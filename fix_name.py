with open('dashboard.html', 'r') as f:
    content = f.read()

old = """  var nameEl = document.getElementById('ob-creator-name-label');
  if (nameEl) {
    var displayName = creatorName || sessionStorage.getItem('tc_last_email') || 'Your profile';
    // Clean up long names
    if (displayName.length > 40) displayName = displayName.substring(0, 40) + '...';
    nameEl.textContent = displayName;
  }"""

new = """  var nameEl = document.getElementById('ob-creator-name-label');
  if (nameEl) {
    // Clean up bad names from backend
    var badNames = ['Loading...', 'loading...', '', null, undefined];
    var cleanName = (badNames.indexOf(creatorName) === -1) ? creatorName : null;
    // Fall back to domain name from URL
    if (!cleanName) {
      var sourceUrl = sessionStorage.getItem('tc_source_url') || '';
      try {
        cleanName = new URL(sourceUrl).hostname.replace('www.','');
      } catch(e) {
        cleanName = sessionStorage.getItem('tc_last_email') || 'Your profile';
      }
    }
    if (cleanName.length > 40) cleanName = cleanName.substring(0, 40) + '...';
    nameEl.textContent = cleanName;
  }"""

result = content.replace(old, new)
print('Fixed:', result != content)
with open('dashboard.html', 'w') as f:
    f.write(result)
