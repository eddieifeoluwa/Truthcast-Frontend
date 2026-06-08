with open('dashboard.html', 'r') as f:
    content = f.read()

# Replace obInit with a dead simple version
old = """function obInit() {
  var token = sessionStorage.getItem('tc_token');
  var onboarded = sessionStorage.getItem('tc_onboarded');
  var scanData = sessionStorage.getItem('tc_scan_data');
  var sourceUrl = sessionStorage.getItem('tc_source_url');
  var savedUserId = sessionStorage.getItem('tc_user_id');
  var user = null;
  try { user = JSON.parse(sessionStorage.getItem('tc_user') || 'null'); } catch(e){}

  if (!token) return;

  // Get current user ID
  var currentUserId = user ? (user.id || user.email || '') : '';

  // If onboarded flag set BUT for a different user → clear and re-onboard
  if (onboarded && savedUserId && currentUserId && savedUserId !== currentUserId) {
    sessionStorage.removeItem('tc_onboarded');
    sessionStorage.removeItem('tc_scan_data');
    sessionStorage.removeItem('tc_source_url');
    sessionStorage.removeItem('tc_source_type');
    sessionStorage.removeItem('tc_source_urls');
    onboarded = null;
    scanData = null;
  }

  // Save current user ID
  if (currentUserId) sessionStorage.setItem('tc_user_id', currentUserId);

  // Already onboarded for this user → skip
  if (onboarded) return;

  // Has scan data for this session → mark onboarded and skip
  if (scanData && sourceUrl) {
    sessionStorage.setItem('tc_onboarded', 'true');
    // Wire the saved data
    try {
      obScanData = JSON.parse(scanData);
      setTimeout(obWireDashboard, 300);
    } catch(e){}
    return;
  }

  // No scan data → show onboarding
  obShowOnboarding(user);
}"""

new = """function obInit() {
  var token = sessionStorage.getItem('tc_token');
  if (!token) return;
  var onboarded = sessionStorage.getItem('tc_onboarded');
  if (onboarded) return;
  var scanData = sessionStorage.getItem('tc_scan_data');
  var sourceUrl = sessionStorage.getItem('tc_source_url');
  if (scanData && sourceUrl) {
    try { obScanData = JSON.parse(scanData); setTimeout(obWireDashboard, 300); } catch(e){}
    return;
  }
  var user = null;
  try { user = JSON.parse(sessionStorage.getItem('tc_user') || 'null'); } catch(e){}
  obShowOnboarding(user);
}"""

result = content.replace(old, new)
print('Fixed:', result != content)
with open('dashboard.html', 'w') as f:
    f.write(result)
