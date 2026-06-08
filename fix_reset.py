with open('dashboard.html', 'r') as f:
    content = f.read()

idx = content.find('// ── RESET ONBOARDING VIA URL PARAM ──')
end = content.find('})();', idx) + 5
old = content[idx:end]
print("Found old reset block:")
print(old[:200])

new = """// ── RESET ONBOARDING VIA URL PARAM ──
(function() {
  var params = new URLSearchParams(window.location.search);
  if (params.get('onboard') === '1') {
    var keys = ['tc_onboarded','tc_source_url','tc_source_type','tc_source_urls','tc_source_types','tc_scan_data','tc_last_email','tc_user_id'];
    keys.forEach(function(k){ sessionStorage.removeItem(k); });
    window.history.replaceState({}, '', window.location.pathname);
  }
})();"""

result = content.replace(old, new)
print('Fixed:', result != content)
with open('dashboard.html', 'w') as f:
    f.write(result)
