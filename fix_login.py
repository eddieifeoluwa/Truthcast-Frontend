content = open('login.html').read()
old = "body: JSON.stringify({email: email, password: pass})\n    });"
new = """body: JSON.stringify({email: email, password: pass})
    });
    if (res.status === 422) {
      var fd = new URLSearchParams();
      fd.append('username', email);
      fd.append('password', pass);
      res = await fetch(API + '/api/v1/auth/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: fd
      });
    }"""
result = content.replace(old, new, 1)
open('login.html', 'w').write(result)
print('Done, size:', len(result))
