/*
 * TruthCast currency helper.
 *
 * Any element with `data-price-gbp="24.99"` gets its text replaced with the
 * converted amount when the current currency changes. Optional suffix via
 * `data-price-suffix="/mo"` gets appended verbatim.
 *
 * Currency flow:
 *   1. On load, hit /pricing/rates → get { rates, detected_currency }
 *   2. localStorage.tc_currency wins if set (user manually picked)
 *   3. Otherwise use backend's IP-detected currency (NG → NGN, US → USD, etc.)
 *   4. Any element in `.tc-currency-toggle` gets wired up as a picker
 *
 * Frontend-only rounding rules:
 *   GBP: keep 2 decimals              (£24.99)
 *   USD: keep 2 decimals              ($31.74)
 *   NGN: round to nearest 100         (₦52,500)
 *
 * Uses fixed fallback rates if the backend is unreachable so pricing never
 * shows "£24.99 = $NaN" on a page load with slow network.
 */
(function () {
  var API_BASE = 'https://truthcast-production.up.railway.app/api/v1';
  var FALLBACK_RATES = { GBP: 1, USD: 1.27, NGN: 2100 };
  var STORAGE_KEY = 'tc_currency';
  var SUPPORTED = ['GBP', 'USD', 'NGN'];
  var SYMBOL = { GBP: '£', USD: '$', NGN: '₦' };

  var state = {
    rates: FALLBACK_RATES,
    currency: (typeof localStorage !== 'undefined' && localStorage.getItem(STORAGE_KEY)) || 'GBP',
    country:  null,
    ready:    false,
  };

  function _format(gbp, currency) {
    var rate = state.rates[currency] || FALLBACK_RATES[currency] || 1;
    var value = gbp * rate;
    if (currency === 'NGN') {
      // Round to nearest 100 for a clean naira display
      var rounded = Math.round(value / 100) * 100;
      return SYMBOL.NGN + rounded.toLocaleString('en-NG');
    }
    return SYMBOL[currency] + value.toFixed(2);
  }

  function _repaint() {
    var nodes = document.querySelectorAll('[data-price-gbp]');
    for (var i = 0; i < nodes.length; i++) {
      var el = nodes[i];
      var gbp = parseFloat(el.getAttribute('data-price-gbp'));
      if (isNaN(gbp)) continue;
      var suffix = el.getAttribute('data-price-suffix') || '';
      // Dual-display mode — always show £X primary + local currency
      // secondary. Used for headline anchor prices (e.g. Founder Circle)
      // where the marketing message is "£99" and dropping the £ symbol
      // breaks the narrative even when the user prefers NGN/USD.
      if (el.getAttribute('data-price-dual') === 'true' && state.currency !== 'GBP') {
        el.textContent = _format(gbp, 'GBP') + suffix + ' · ≈ ' + _format(gbp, state.currency);
      } else {
        el.textContent = _format(gbp, state.currency) + suffix;
      }
    }
    // Update toggle UI — highlight the selected currency, dim others
    var toggles = document.querySelectorAll('.tc-currency-toggle [data-currency]');
    for (var j = 0; j < toggles.length; j++) {
      var t = toggles[j];
      if (t.getAttribute('data-currency') === state.currency) {
        t.classList.add('tc-currency-active');
      } else {
        t.classList.remove('tc-currency-active');
      }
    }
  }

  function setCurrency(code) {
    if (SUPPORTED.indexOf(code) === -1) return;
    state.currency = code;
    try { localStorage.setItem(STORAGE_KEY, code); } catch (e) {}
    _repaint();
    // Broadcast so pages can react (e.g. dashboard billing card).
    try {
      window.dispatchEvent(new CustomEvent('tc-currency-change', {
        detail: { currency: code, rates: state.rates },
      }));
    } catch (e) {}
  }

  function _wireToggles() {
    var toggles = document.querySelectorAll('.tc-currency-toggle [data-currency]');
    for (var i = 0; i < toggles.length; i++) {
      var t = toggles[i];
      if (t._tcWired) continue;
      t._tcWired = true;
      t.addEventListener('click', function (ev) {
        ev.preventDefault();
        setCurrency(this.getAttribute('data-currency'));
      });
    }
  }

  function init() {
    // Paint whatever we have first — either the last-picked currency from
    // localStorage or the GBP fallback. Then refine after the API call.
    _wireToggles();
    _repaint();

    var already = typeof localStorage !== 'undefined' && localStorage.getItem(STORAGE_KEY);

    fetch(API_BASE + '/pricing/rates', { method: 'GET' })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (res) {
        if (!res || !res.success || !res.data) return;
        var d = res.data;
        if (d.rates) state.rates = d.rates;
        state.country = d.detected_country || null;
        // Only auto-switch if the user has NOT manually picked before.
        if (!already && d.detected_currency && SUPPORTED.indexOf(d.detected_currency) !== -1) {
          state.currency = d.detected_currency;
        }
        state.ready = true;
        _repaint();
      })
      .catch(function () { /* keep fallback state; painted already */ });
  }

  // Expose a tiny API on window so page-specific code can format prices
  // (e.g. the dashboard's Stripe upgrade button that isn't a static DOM node).
  window.TCCurrency = {
    get: function () { return state.currency; },
    setCurrency: setCurrency,
    format: function (gbp) { return _format(gbp, state.currency); },
    rates: function () { return state.rates; },
    // Call after injecting HTML that contains new [data-price-gbp] nodes.
    // Dashboard billing card + upgrade banners inject via innerHTML after
    // /me resolves, well after the initial DOMContentLoaded paint.
    repaint: function () { _wireToggles(); _repaint(); },
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
