with open('login.html', 'r') as f:
    content = f.read()

# Fix 1: signin saves user properly and clears old data
old1 = """    sessionStorage.setItem('tc_token', data.access_token || data.token);
    if (data.user) {
      sessionStorage.setItem('tc_user', JSON.stringify(data.user));
    }"""
new1 = """    sessionStorage.setItem('tc_token', data.access_token || data.token);
    var userData = data.user || {id: data.user_id||data.id, email: data.email, full_name: data.full_name||data.name, profile_type: data.creator_type||'creator', plan: 'free'};
    sessionStorage.setItem('tc_user', JSON.stringify(userData));
    sessionStorage.removeItem('tc_onboarded');
    sessionStorage.removeItem('tc_scan_data');
    sessionStorage.removeItem('tc_source_url');
    sessionStorage.removeItem('tc_source_type');
    sessionStorage.removeItem('tc_last_email');"""
content = content.replace(old1, new1)

# Fix 2: auto-login after register saves user properly
old2 = """      sessionStorage.setItem('tc_token', loginData.access_token || loginData.token);
      if (loginData.user) {
        sessionStorage.setItem('tc_user', JSON.stringify(loginData.user));
      }"""
new2 = """      sessionStorage.setItem('tc_token', loginData.access_token || loginData.token);
      var lu = loginData.user || {id: loginData.user_id||loginData.id, email: loginData.email, full_name: loginData.full_name||loginData.name, profile_type: loginData.creator_type||'creator', plan: 'free'};
      sessionStorage.setItem('tc_user', JSON.stringify(lu));
      sessionStorage.removeItem('tc_onboarded');
      sessionStorage.removeItem('tc_scan_data');
      sessionStorage.removeItem('tc_source_url');
      sessionStorage.removeItem('tc_last_email');"""
content = content.replace(old2, new2)

with open('login.html', 'w') as f:
    f.write(content)
print('Fix 1:', 'userData = data.user ||' in content)
print('Fix 2:', 'lu = loginData.user ||' in content)
