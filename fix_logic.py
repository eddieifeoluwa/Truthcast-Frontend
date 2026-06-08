with open('login.html', 'r') as f:
    content = f.read()

# For REGISTER: clear everything (new user needs onboarding)
# For LOGIN: keep scan data (returning user should skip onboarding)

# Fix register handler - CLEAR scan data (new user)
old_reg = """    sessionStorage.setItem('tc_user', JSON.stringify(userData));
    sessionStorage.removeItem('tc_onboarded');
    sessionStorage.removeItem('tc_scan_data');
    sessionStorage.removeItem('tc_source_url');
    sessionStorage.removeItem('tc_source_type');
    sessionStorage.removeItem('tc_last_email');

    showBanner('signin-ok', '✓ Account created! Setting up your dashboard...');"""

new_reg = """    sessionStorage.setItem('tc_user', JSON.stringify(userData));
    // New user - clear everything so onboarding shows
    sessionStorage.removeItem('tc_onboarded');
    sessionStorage.removeItem('tc_scan_data');
    sessionStorage.removeItem('tc_source_url');
    sessionStorage.removeItem('tc_source_type');
    sessionStorage.removeItem('tc_last_email');
    sessionStorage.setItem('tc_is_new_user', 'true');

    showBanner('signin-ok', '✓ Account created! Setting up your dashboard...');"""

content = content.replace(old_reg, new_reg)
print('Reg fix:', 'tc_is_new_user' in content)

# Fix auto-login after register - KEEP the new user flag
old_auto = """      sessionStorage.setItem('tc_user', JSON.stringify(lu));
      sessionStorage.removeItem('tc_onboarded');
      sessionStorage.removeItem('tc_scan_data');
      sessionStorage.removeItem('tc_source_url');
      sessionStorage.removeItem('tc_last_email');"""

new_auto = """      sessionStorage.setItem('tc_user', JSON.stringify(lu));
      // Keep tc_is_new_user flag set by register"""

content = content.replace(old_auto, new_auto)
print('Auto fix:', 'Keep tc_is_new_user' in content)

with open('login.html', 'w') as f:
    f.write(content)
