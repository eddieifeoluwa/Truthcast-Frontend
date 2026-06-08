with open('dashboard.html', 'r') as f:
    content = f.read()

old = """// ── RESET ONBOARDING VIA URL PARAM ──
(function() {
  var params = new URLSearchParams(window.location.search);
  if (params.get('onboard') === '1') {
    sessionStorage.removeItem('tc_onboarded');
    sessionStorage.removeItem('tc_source_url');
    sessionStorage.removeItem('tc_scan_data');
    // Remove param from URL without reload
    var url = window.location.pathname;
    window.history.replaceState({}, '', url);
  }
})();"""

new = """// ── RESET ONBOARDING VIA URL PARAM ──
(function() {
  var params = new URLSearchParams(window.location.search);
  if (params.get('onboard') === '1') {
    sessionStorage.removeItem('tc_onboarded');
    sessionStorage.removeItem('tc_source_url');
    sessionStorage.removeItem('tc_source_type');
    sessionStorage.removeItem('tc_source_urls');
    sessionStorage.removeItem('tc_source_types');
    sessionStorage.removeItem('tc_scan_data');
    sessionStorage.removeItem('tc_last_email');
    sessionStorage.removeItem('tc_user_id');
    var url = window.location.pathname;
    window.history.replaceState({}, '', url);
  }
})();"""

result = content.replace(old, new)
print('Fixed:', result != content)
with open('dashboard.html', 'w') as f:
    f.write(result)
