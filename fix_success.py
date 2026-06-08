with open('dashboard.html', 'r') as f:
    content = f.read()

# Fix 1: creator name showing "Loading..."
# Find obShowSuccess and fix creator name
old_name = "  document.getElementById('ob-creator-name-label').textContent = creatorName;"
new_name = """  var nameEl = document.getElementById('ob-creator-name-label');
  if (nameEl) {
    var displayName = creatorName || sessionStorage.getItem('tc_last_email') || 'Your profile';
    // Clean up long names
    if (displayName.length > 40) displayName = displayName.substring(0, 40) + '...';
    nameEl.textContent = displayName;
  }"""
content = content.replace(old_name, new_name)
print('Name fix:', 'displayName' in content)

# Fix 2: content label showing "Reports" for brand URLs
# The ob-content-label update needs to happen in obShowSuccess too
old_content_label = """  var contentLabelEl = document.getElementById('ob-content-label');
  if (contentLabelEl) {
    var contentLabels = {
      podcast:'Episodes', youtube:'Videos', tiktok:'Posts',
      musician:'Releases', blogger:'Posts', tvhost:'Episodes',
      journalist:'Articles', educator:'Courses', professional:'Posts',
      publicfigure:'Mentions', ceo:'Pages', politician:'Mentions',
      brand:'Pages', mediahouse:'Articles', healthcare:'Pages',
      religious:'Content', school:'Pages', ngo:'Reports'
    };
    contentLabelEl.textContent = contentLabels[obSourceType] || 'Content';
  }"""

new_content_label = """  var contentLabelEl = document.getElementById('ob-content-label');
  if (contentLabelEl) {
    var contentLabels = {
      podcast:'Episodes', youtube:'Videos', tiktok:'Posts',
      musician:'Releases', blogger:'Posts', tvhost:'Episodes',
      journalist:'Articles', educator:'Courses', professional:'Posts',
      publicfigure:'Mentions', ceo:'Pages', politician:'Mentions',
      brand:'Pages', mediahouse:'Articles', healthcare:'Pages',
      religious:'Content', school:'Pages', ngo:'Pages'
    };
    // Use detected source type not input type
    var detectedType = obSourceType || 'brand';
    contentLabelEl.textContent = contentLabels[detectedType] || 'Pages';
  }"""

content = content.replace(old_content_label, new_content_label)
print('Label fix:', "ngo:'Pages'" in content)

with open('dashboard.html', 'w') as f:
    f.write(content)
