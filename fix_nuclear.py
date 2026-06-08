with open('dashboard.html', 'r') as f:
    content = f.read()

old = """(function() {
  var params = new URLSearchParams(window.location.search);
  if (params.get('onboard') === '1') {
    sessionStorage.clear();
    window.history.replaceState({}, '', window.location.pathname);
    window.location.reload();
  }
})();"""

# Check if already updated
if old in content:
    print('Already updated')
else:
    old2 = """(function() {
  var params = new URLSearchParams(window.location.search);
  if (params.get('onboard') === '1') {
    var keys = ['tc_onboarded','tc_source_url','tc_source_type','tc_source_urls','tc_source_types','tc_scan_data','tc_last_email','tc_user_id'];
    keys.forEach(function(k){ sessionStorage.removeItem(k); });
    window.history.replaceState({}, '', window.location.pathname);
  }
})();"""
    result = content.replace(old2, old)
    print('Fixed:', result != content)
    with open('dashboard.html', 'w') as f:
        f.write(result)
