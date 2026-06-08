with open('dashboard.html', 'r') as f:
    content = f.read()

# Fix obWireDashboard to clean bad creator names
old = """  var score      = obScanData.trust_score || obScanData.overall_trust_score || 84;
  var grade      = obScanData.overall_grade || obScanData.grade || 'A';
  var total      = obScanData.total_content || 0;
  var creatorName = obScanData.creator_name || '';
  var sourceType = sessionStorage.getItem('tc_source_type') || 'creator';"""

new = """  var score      = obScanData.trust_score || obScanData.overall_trust_score || 84;
  var grade      = obScanData.overall_grade || obScanData.grade || 'A';
  var total      = obScanData.total_content || 0;
  var sourceType = sessionStorage.getItem('tc_source_type') || 'creator';
  // Clean bad creator names from backend
  var rawName = obScanData.creator_name || '';
  var badNames = ['Loading...', 'loading...', 'undefined', 'null'];
  var creatorName = (badNames.indexOf(rawName) === -1 && rawName.length > 0) ? rawName : '';
  if (!creatorName) {
    var sourceUrl = sessionStorage.getItem('tc_source_url') || '';
    try { creatorName = new URL(sourceUrl).hostname.replace('www.',''); } catch(e) {}
  }"""

result = content.replace(old, new)
print('Fixed:', result != content)
with open('dashboard.html', 'w') as f:
    f.write(result)
