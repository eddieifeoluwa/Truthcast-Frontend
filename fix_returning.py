with open('login.html', 'r') as f:
    content = f.read()

# The signin handler should NEVER clear tc_onboarded
# Only register should clear it
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
    // Never clear scan data on signin - returning users keep their data
    sessionStorage.setItem('tc_last_email', userData.email || '');"""

result = content.replace(old, new)
print('Fixed:', result != content)
with open('login.html', 'w') as f:
    f.write(result)
