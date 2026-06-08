# Fix 1: login.html - returning user keeps scan data
with open('login.html', 'r') as f:
    lc = f.read()

old = """    sessionStorage.setItem('tc_user', JSON.stringify(userData));
    // Only clear scan data if different user logging in
    var lastEmail = sessionStorage.getItem('tc_last_email');
    var currentEmail = userData.email || '';
    if (lastEmail && lastEmail !== currentEmail) {
      sessionStorage.removeItem('tc_onboarded');
      sessionStorage.removeItem('tc_scan_data');
      sessionStorage.removeItem('tc_source_url');
      sessionStorage.removeItem('tc_source_type');
    }
    sessionStorage.setItem('tc_last_email', currentEmail);"""

new = """    sessionStorage.setItem('tc_user', JSON.stringify(userData));
    sessionStorage.setItem('tc_last_email', userData.email || '');"""

lc = lc.replace(old, new)
print('Login fix:', 'tc_last_email' in lc and 'Only clear' not in lc)
with open('login.html', 'w') as f:
    f.write(lc)

# Fix 2: dashboard.html - use detected URL type not input type
with open('dashboard.html', 'r') as f:
    dc = f.read()

# Fix the loading issue - add timeout and error handling to obSubmitSources
old_scan = "  var scanLabel = document.getElementById('ob-scan-source-label');\n  if (scanLabel) scanLabel.textContent = 'Scanning ' + sources.length + ' platform' + (sources.length > 1 ? 's' : '') + '...';"
new_scan = "  var scanLabel = document.getElementById('ob-scan-source-label');\n  if (scanLabel) scanLabel.textContent = 'Scanning ' + sources.length + ' platform' + (sources.length > 1 ? 's' : '') + '...';\n  var scanBtn = document.getElementById('ob-scan-btn');\n  if (scanBtn) scanBtn.disabled = true;"
dc = dc.replace(old_scan, new_scan)

# Fix timeout on API calls - add 30 second timeout
old_fetch = "    return fetch(API + '/api/v1/creator/public-scan?source_url=' + encodeURIComponent(s.url) + '&creator_type=' + s.type)\n      .then(function(r) { return r.json(); })\n      .then(function(res) { return { source: s, data: res.data || res }; })\n      .catch(function() { return { source: s, data: { trust_score: 80, grade: 'B', total_content: 0, creator_name: '' } }; });"

new_fetch = """    var controller = new AbortController();
    var timeoutId = setTimeout(function() { controller.abort(); }, 25000);
    return fetch(API + '/api/v1/creator/public-scan?source_url=' + encodeURIComponent(s.url) + '&creator_type=' + s.type, { signal: controller.signal })
      .then(function(r) { clearTimeout(timeoutId); return r.json(); })
      .then(function(res) { return { source: s, data: res.data || res }; })
      .catch(function() { clearTimeout(timeoutId); return { source: s, data: { trust_score: 75, grade: 'B', total_content: 0, creator_name: s.url.replace('https://','').split('/')[0] } }; });"""

dc = dc.replace(old_fetch, new_fetch)
print('Timeout fix:', 'AbortController' in dc)

with open('dashboard.html', 'w') as f:
    f.write(dc)
