with open('login.html', 'r') as f:
    content = f.read()

old = """    // Auto sign-in after register
    showBanner('reg-ok', '✓ Account created! Signing you in...');
    var loginRes = await fetch(API + '/api/v1/auth/login', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({email: email, password: pass})
    });
    var loginData = await loginRes.json();
    if (loginRes.ok) {
      sessionStorage.setItem('tc_token', loginData.access_token || loginData.token);
      var lu = loginData.user || {id: loginData.user_id||loginData.id, email: loginData.email, full_name: loginData.full_name||loginData.name, profile_type: loginData.creator_type||'creator', plan: 'free'};
      sessionStorage.setItem('tc_user', JSON.stringify(lu));
      // Keep tc_is_new_user flag set by register
    }

    setTimeout(function() { window.location.href = 'dashboard.html'; }, 1000);"""

new = """    // Auto sign-in after register using form-encoded
    showBanner('reg-ok', '✓ Account created! Signing you in...');
    var fd = new URLSearchParams();
    fd.append('username', email);
    fd.append('password', pass);
    var loginRes = await fetch(API + '/api/v1/auth/login', {
      method: 'POST',
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      body: fd
    });
    var loginData = await loginRes.json();
    if (loginRes.ok) {
      // Save token and user
      sessionStorage.setItem('tc_token', loginData.access_token || loginData.token);
      var lu = loginData.user || {id: loginData.user_id||loginData.id, email: loginData.email, full_name: loginData.full_name||loginData.name, profile_type: loginData.creator_type||'creator', plan: 'free'};
      sessionStorage.setItem('tc_user', JSON.stringify(lu));
      // Clear scan data so new user sees onboarding
      sessionStorage.removeItem('tc_onboarded');
      sessionStorage.removeItem('tc_scan_data');
      sessionStorage.removeItem('tc_source_url');
      sessionStorage.removeItem('tc_source_type');
      sessionStorage.removeItem('tc_last_email');
    }

    setTimeout(function() { window.location.href = 'dashboard.html'; }, 1000);"""

result = content.replace(old, new)
print('Fixed:', result != content)
with open('login.html', 'w') as f:
    f.write(result)
