with open('dashboard.html', 'r') as f:
    content = f.read()

old = """  if (scanData && sourceUrl) {
    try { obScanData = JSON.parse(scanData); setTimeout(obWireDashboard, 300); } catch(e){}
    return;
  }"""

new = """  if (scanData && sourceUrl) {
    try {
      obScanData = JSON.parse(scanData);
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
