with open('dashboard.html', 'r') as f:
    content = f.read()

# After obCombineScores, force re-detect from actual URL
old = """      var combined = obCombineScores(results);
      obScanData = combined;
      // Save all sources
      sessionStorage.setItem('tc_source_urls', JSON.stringify(sources.map(function(s){return s.url;})));
      sessionStorage.setItem('tc_source_types', JSON.stringify(sources.map(function(s){return s.type;})));
      sessionStorage.setItem('tc_source_url', sources[0].url);
      // Save AFTER obCombineScores has set correct obSourceType
      sessionStorage.setItem('tc_source_type', obSourceType);"""

new = """      var combined = obCombineScores(results);
      obScanData = combined;
      // Always re-detect type from actual URL
      var detectedFromUrl = detectUrlType(sources[0].url);
      obSourceType = detectedFromUrl;
      combined.creator_type = detectedFromUrl;
      // Save all sources
      sessionStorage.setItem('tc_source_urls', JSON.stringify(sources.map(function(s){return s.url;})));
      sessionStorage.setItem('tc_source_types', JSON.stringify(sources.map(function(s){return s.type;})));
      sessionStorage.setItem('tc_source_url', sources[0].url);
      sessionStorage.setItem('tc_source_type', detectedFromUrl);"""

result = content.replace(old, new)
print('Fixed:', result != content)
with open('dashboard.html', 'w') as f:
    f.write(result)
