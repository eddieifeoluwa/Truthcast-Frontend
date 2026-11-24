/* TruthCast shared site script: header, footer, reveal animations, pricing currency, article cards. */
(function () {
  const page = document.body.dataset.page || '';

  const shield = `<svg width="0" height="0" style="position:absolute" aria-hidden="true">
    <symbol id="shield" viewBox="0 0 40 46">
      <path d="M20 2 37 8v14c0 11-7.4 18.6-17 22C10.4 40.6 3 33 3 22V8z" fill="#0b0a08" stroke="#b8e03a" stroke-width="3.2"/>
      <path d="M11 13h18v5h-6.3v16h-5.4V18H11z" fill="#f4efe6"/>
    </symbol></svg>`;

  const links = [
    ['home', 'index.html', 'Home'],
    ['story', 'story.html', 'Our Story'],
    ['voices', 'voices.html', 'Who We Serve'],
    ['articles', 'articles.html', 'Articles'],
    ['pricing', 'index.html#pricing', 'Pricing']
  ];

  const header = document.getElementById('site-header');
  if (header) {
    header.outerHTML = `${shield}
    <div class="announce">Build your legacy · Understand your impact <a href="index.html#founding">Join the first 100 →</a></div>
    <nav>
      <div class="wrap">
        <a href="index.html" class="logo"><svg class="shield"><use href="#shield"/></svg><span>Truth<b>Cast</b></span></a>
        <div class="nav-links" id="nav-links">
          ${links.map(([k, href, label]) => `<a href="${href}"${k === page ? ' class="on" aria-current="page"' : ''}>${label}</a>`).join('')}
          <a class="mob-only" href="/login.html">Sign in</a>
          <a class="mob-only mob-cta" href="/onboarding.html">Get early access →</a>
        </div>
        <div class="nav-cta">
          <a class="signin" href="/login.html">SIGN IN</a>
          <a class="btn btn-lime" href="/onboarding.html">Get early access</a>
          <button class="menu-btn" aria-label="Open menu" aria-expanded="false"><span></span><span></span></button>
        </div>
      </div>
    </nav>`;
    const btn = document.querySelector('.menu-btn');
    const nl = document.getElementById('nav-links');
    btn.addEventListener('click', () => {
      const open = nl.classList.toggle('open');
      btn.setAttribute('aria-expanded', open);
    });
  }

  const footer = document.getElementById('site-footer');
  if (footer) {
    const credits = [
      ['easyshay', 'Ezekiel Nuhu'], ['tony1218', 'Tony Chen'], ['anniespratt', 'Annie Spratt'], ['v2osk', 'v2osk'],
      ['princearkman', 'Prince Akachi'], ['expressee', 'Belinda Amoah'], ['lucasgouvea', 'Lucas Gouvêa'],
      ['charlesdeluvio', 'charlesdeluvio'], ['katiemoum', 'Katie Moum'], ['bogomi', 'Bogomil Mihaylov'], ['baohoang04', 'Bao Hoang'], ['jukkaaalho', 'Jukka Aalho']
    ].map(([u, n]) => `<a href="https://unsplash.com/@${u}?utm_source=truthcast&utm_medium=referral">${n}</a>`).join(', ');
    footer.outerHTML = `<footer>
      <div class="wrap">
        <div class="foot">
          <div><a href="index.html" class="logo"><svg class="shield"><use href="#shield"/></svg><span>Truth<b>Cast</b></span></a>
            <p>Reputation intelligence for public voices, podcasters and brands. Build your legacy. Understand your impact. Your reputation is your asset.</p></div>
          <div><h4>PLATFORM</h4><ul><li><a href="index.html#how">How it works</a></li><li><a href="voices.html">Public voices</a></li><li><a href="voices.html#podcasters">Podcasters</a></li><li><a href="voices.html#founders">Founders &amp; leaders</a></li><li><a href="voices.html#brands">Brands</a></li><li><a href="index.html#pricing">Pricing</a></li><li><a href="index.html#founding">Founding members</a></li></ul></div>
          <div><h4>READ</h4><ul><li><a href="articles.html">All articles</a></li><li><a href="articles.html?c=Reputation">Reputation</a></li><li><a href="articles.html?c=Legacy">Legacy</a></li><li><a href="articles.html?c=Perception">Perception</a></li></ul></div>
          <div><h4>COMPANY</h4><ul><li><a href="story.html">Our story</a></li><li><a href="mailto:hello@truthcast.io">Contact</a></li><li><a href="/privacy.html">Privacy</a></li><li><a href="/terms.html">Terms</a></li></ul></div>
        </div>
        <div class="credits">
          <span>© 2026 TruthCast Ltd. London, UK · hello@truthcast.io</span>
          <span>Stock photos on <a href="https://unsplash.com/?utm_source=truthcast&utm_medium=referral">Unsplash</a> by ${credits}</span>
        </div>
      </div>
    </footer>`;
  }

  /* Digital Trust seal: any element with class "seal" gets the gold rotating seal */
  document.querySelectorAll('.seal').forEach((el, i) => {
    const id = 'seal' + i;
    el.innerHTML = `<svg viewBox="0 0 200 200" role="img" aria-label="TruthCast seal: Digital Trust for the People">
      <defs>
        <linearGradient id="${id}g" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="#f8dc98"/><stop offset=".45" stop-color="#d9a55b"/><stop offset=".75" stop-color="#a8742f"/><stop offset="1" stop-color="#f0c27f"/>
        </linearGradient>
        <radialGradient id="${id}c" cx=".5" cy=".38" r=".7">
          <stop offset="0" stop-color="#231d12"/><stop offset="1" stop-color="#0b0a08"/>
        </radialGradient>
        <path id="${id}p" d="M100,100 m-74,0 a74,74 0 1,1 148,0 a74,74 0 1,1 -148,0"/>
      </defs>
      <circle cx="100" cy="100" r="98" fill="url(#${id}g)"/>
      <circle cx="100" cy="100" r="92" fill="none" stroke="#0b0a08" stroke-opacity=".35" stroke-width="1"/>
      <g class="seal-spin">
        <circle cx="100" cy="100" r="88" fill="none" stroke="#0b0a08" stroke-opacity=".5" stroke-width="1" stroke-dasharray="1 4"/>
        <text font-family="JetBrains Mono, monospace" font-size="12.5" font-weight="500" fill="#1a1308" letter-spacing="2">
          <textPath href="#${id}p" textLength="462" lengthAdjust="spacing">DIGITAL TRUST FOR THE PEOPLE ✦ TRUTHCAST ✦ </textPath>
        </text>
      </g>
      <circle cx="100" cy="100" r="58" fill="url(#${id}c)" stroke="url(#${id}g)" stroke-width="3"/>
      <circle cx="100" cy="100" r="52" fill="none" stroke="#d9a55b" stroke-opacity=".35" stroke-width="1"/>
      <use href="#shield" x="80" y="68" width="40" height="46"/>
      <text x="100" y="134" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="7.5" letter-spacing="2.2" fill="#f0c27f">DIGITAL TRUST</text>
    </svg>`;
  });

  /* Article cards: any element with data-articles="N" (optionally data-exclude="slug") is filled from TC_ARTICLES */
  window.tcCard = function (a) {
    return `<a class="post rv" href="article.html?a=${a.slug}">
      <div class="post-img"><img src="${a.cover}" alt="${a.coverAlt}" loading="lazy"></div>
      <div class="post-body">
        <div class="post-meta"><span>${a.category}</span><span>${a.readTime} min read</span></div>
        <h3>${a.title}</h3>
        <p>${a.excerpt}</p>
      </div>
    </a>`;
  };
  if (window.TC_ARTICLES) {
    document.querySelectorAll('[data-articles]').forEach(el => {
      const n = +el.dataset.articles || 3;
      const ex = el.dataset.exclude;
      el.innerHTML = TC_ARTICLES.filter(a => a.slug !== ex).slice(0, n).map(tcCard).join('');
    });
  }

  /* Reveal on scroll */
  window.tcReveal = function () {
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .12 });
    document.querySelectorAll('.rv:not(.in)').forEach(el => io.observe(el));
  };

  /* Pricing currency toggle — each price carries the owner's real amount per
     currency (data-gbp / data-usd / data-ngn), same figures as the previous
     truthcast.io pricing. Choice persists in tc_currency, shared with the app. */
  const sym = { gbp: '£', usd: '$', ngn: '₦' };
  function applyCurrency(c) {
    if (!sym[c]) c = 'gbp';
    document.querySelectorAll('.cur button').forEach(x => x.classList.toggle('on', x.dataset.c === c));
    document.querySelectorAll('[data-gbp]').forEach(el => {
      const v = +(el.dataset[c] || el.dataset.gbp);
      el.textContent = sym[c] + v.toLocaleString();
    });
    try { localStorage.setItem('tc_currency', c.toUpperCase()); } catch (_) {}
  }
  document.querySelectorAll('.cur button').forEach(b => b.addEventListener('click', () => applyCurrency(b.dataset.c)));
  if (document.querySelector('.cur')) {
    let saved = 'gbp';
    try { saved = (localStorage.getItem('tc_currency') || 'GBP').toLowerCase(); } catch (_) {}
    applyCurrency(saved);
  }

  /* Founding member: live spots counter + Stripe checkout */
  const API = 'https://truthcast-production.up.railway.app/api/v1';
  const spotsText = document.getElementById('fc-spots-text');
  const spotsBar = document.getElementById('fc-spots-bar');
  const claim = document.getElementById('fc-claim');
  if (spotsText || claim) {
    fetch(API + '/payments/founder-circle/status')
      .then(r => r.ok ? r.json() : null)
      .then(res => {
        if (!res || !res.success || !res.data) throw 0;
        const d = res.data;
        if (spotsBar) spotsBar.style.width = Math.max(3, Math.round((d.taken / d.cap) * 100)) + '%';
        if (d.sold_out) {
          if (spotsText) spotsText.textContent = 'SOLD OUT · ALL ' + d.cap + ' CLAIMED';
          if (claim) { claim.textContent = 'Join the waitlist →'; claim.href = 'mailto:hello@truthcast.io?subject=Founding%20member%20waitlist'; claim.dataset.soldOut = '1'; }
        } else if (spotsText) {
          spotsText.textContent = d.remaining + ' OF ' + d.cap + ' FOUNDING SPOTS REMAINING';
        }
      })
      .catch(() => { if (spotsText) spotsText.textContent = 'LIMITED SPOTS REMAINING'; });
  }
  if (claim) claim.addEventListener('click', e => {
    if (claim.dataset.soldOut) return;
    e.preventDefault();
    let token = null;
    try { token = localStorage.getItem('tc_token'); } catch (_) {}
    if (!token) {
      // Checkout needs an account. The dashboard picks this flag up after
      // sign-in / sign-up and opens Stripe automatically.
      try { localStorage.setItem('tc_pending_founder', '1'); } catch (_) {}
      window.location.href = '/login.html';
      return;
    }
    const label = claim.textContent;
    claim.textContent = 'Opening secure checkout…';
    fetch(API + '/payments/founder-circle/checkout', { method: 'POST', headers: { Authorization: 'Bearer ' + token } })
      .then(r => r.json().then(b => ({ s: r.status, b })))
      .then(({ s, b }) => {
        if (s === 200 && b.success && b.data && b.data.checkout_url) { window.location.href = b.data.checkout_url; return; }
        if (s === 401) {
          try { localStorage.setItem('tc_pending_founder', '1'); } catch (_) {}
          window.location.href = '/login.html';
          return;
        }
        claim.textContent = label;
        const note = document.getElementById('fc-note');
        if (note) note.textContent = s === 409 ? 'All 100 founding spots have been claimed.' : (b.detail || 'Checkout could not start. Please try again.');
      })
      .catch(() => { claim.textContent = label; });
  });

  document.addEventListener('DOMContentLoaded', () => window.tcReveal());
  if (document.readyState !== 'loading') window.tcReveal();
})();
