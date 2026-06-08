with open('dashboard.html', 'r') as f:
    content = f.read()

# Fix: In obInit, re-detect type from saved URL
old = """  // Has scan data for this session → mark onboarded and skip
  if (scanData && sourceUrl) {
    try { obScanData = JSON.parse(scanData); setTimeout(obWireDashboard, 300); } catch(e){}
    return;
  }"""

new = """  // Has scan data for this session → wire dashboard
  if (scanData && sourceUrl) {
    try {
      obScanData = JSON.parse(scanData);
      // Re-detect type from actual URL to override stale sessionStorage
      var reDetected = detectUrlType(sourceUrl);
      if (reDetected) {
        obSourceType = reDetected;
        sessionStorage.setItem('tc_source_type', reDetected);
      }
      setTimeout(obWireDashboard, 300);
    } catch(e){}
    return;
  }"""

result = content.replace(old, new)
print('Fixed:', result != content)
with open('dashboard.html', 'w') as f:
    f.write(result)
