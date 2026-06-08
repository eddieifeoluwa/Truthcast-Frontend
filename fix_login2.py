with open('login.html', 'r') as f:
    content = f.read()

# Fix the login to use form-encoded with username field first
old_login_fetch = """    var res = await fetch(API + '/api/v1/auth/login', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({email: email, password: pass})
    });
    // If JSON fails with validation error, fall back to form-encoded with username field
    if (!res.ok) {
      var errData = await res.json();
      if (errData.detail && JSON.stringify(errData.detail).includes('Field required')) {
        var formData = new URLSearchParams();
        formData.append('username', email);
        formData.append('password', pass);
        res = await fetch(API + '/api/v1/auth/login', {
          method: 'POST',
          headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          body: formData
        });
      }
    }"""

new_login_fetch = """    // Use form-encoded with username field (FastAPI OAuth2 format)
    var formData = new URLSearchParams();
    formData.append('username', email);
    formData.append('password', pass);
    var res = await fetch(API + '/api/v1/auth/login', {
      method: 'POST',
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      body: formData
    });
    // Fallback to JSON if form fails
    if (!res.ok) {
      res = await fetch(API + '/api/v1/auth/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({email: email, password: pass})
      });
    }"""

result = content.replace(old_login_fetch, new_login_fetch)
if result == content:
    print("Pattern not found - trying alternative")
    # Find and show the login fetch area
    idx = content.find('/api/v1/auth/login')
    print(content[idx-100:idx+300])
else:
    print("Login fetch fixed:", 'username' in result)
    with open('login.html', 'w') as f:
        f.write(result)
