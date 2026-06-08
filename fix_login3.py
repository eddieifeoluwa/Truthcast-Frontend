with open('login.html', 'r') as f:
    content = f.read()

old = """    var res = await fetch(API + '/api/v1/auth/login', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({email: email, password: pass})
    });
    var data = await res.json();"""

new = """    var fd = new URLSearchParams();
    fd.append('username', email);
    fd.append('password', pass);
    var res = await fetch(API + '/api/v1/auth/login', {
      method: 'POST',
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      body: fd
    });
    if (!res.ok) {
      res = await fetch(API + '/api/v1/auth/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({email: email, password: pass})
      });
    }
    var data = await res.json();"""

result = content.replace(old, new)
print('Fixed:', result != content)
with open('login.html', 'w') as f:
    f.write(result)
