with open('login.html', 'r') as f:
    content = f.read()

# Signin should NOT clear scan data for returning users
old = """    sessionStorage.setItem('tc_token', data.access_token || data.token);
    var userData = data.user || {id: data.user_id||data.id, email: data.email, full_name: data.full_name||data.name, profile_type: data.creator_type||'creator', plan: 'free'};
    sessionStorage.setItem('tc_user', JSON.stringify(userData));
    sessionStorage.removeItem('tc_onboarded');
    sessionStorage.removeItem('tc_scan_data');
    sessionStorage.removeItem('tc_source_url');
    sessionStorage.removeItem('tc_source_type');
    sessionStorage.removeItem('tc_last_email');"""

new = """    sessionStorage.setItem('tc_token', data.access_token || data.token);
    var userData = data.user || {id: data.user_id||data.id, email: data.email, full_name: data.full_name||data.name, profile_type: data.creator_type||'creator', plan: 'free'};
    sessionStorage.setItem('tc_user', JSON.stringify(userData));
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

result = content.replace(old, new)
print('Fixed:', result != content)
with open('login.html', 'w') as f:
    f.write(result)
