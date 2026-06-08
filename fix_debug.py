with open('dashboard.html', 'r') as f:
    content = f.read()

old = """(function() {
  var params = new URLSearchParams(window.location.search);
  if (params.get('onboard') === '1') {
    sessionStorage.clear();
    window.history.replaceState({}, '', window.location.pathname);
    window.location.reload();
  }
})();"""

new = """(function() {
  var params = new URLSearchParams(window.location.search);
  if (params.get('onboard') === '1') {
    sessionStorage.clear();
    window.location.href = window.location.pathname;
    return;
  }
  if (params.get('logout') === '1') {
    sessionStorage.clear();
    window.location.href = '/login.html';
    return;
  }
})();"""

result = content.replace(old, new)
print('Fixed:', result != content)
with open('dashboard.html', 'w') as f:
    f.write(result)
