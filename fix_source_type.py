with open('dashboard.html', 'r') as f:
    content = f.read()

# Remove early save of tc_source_type
old = """  // Set primary source (first filled)
  obSourceType = sources[0].type;
  sessionStorage.setItem('tc_source_type', obSourceType);"""

new = """  // Set primary source (will be overridden by URL detection in obCombineScores)
  obSourceType = sources[0].type;"""

content = content.replace(old, new)

# Make sure tc_source_type is saved AFTER combine (in obShowSuccess)
old_show = """  sessionStorage.setItem('tc_source_urls', JSON.stringify(sources.map(function(s){return s.url;})));
      sessionStorage.setItem('tc_source_types', JSON.stringify(sources.map(function(s){return s.type;})));
      sessionStorage.setItem('tc_source_url', sources[0].url);
      sessionStorage.setItem('tc_source_type', obSourceType);
      sessionStorage.setItem('tc_scan_data', JSON.stringify(combined));
      obShowSuccess(sources[0].url, combined);"""

new_show = """  sessionStorage.setItem('tc_source_urls', JSON.stringify(sources.map(function(s){return s.url;})));
      sessionStorage.setItem('tc_source_types', JSON.stringify(sources.map(function(s){return s.type;})));
      sessionStorage.setItem('tc_source_url', sources[0].url);
      // Save AFTER obCombineScores has set correct obSourceType
      sessionStorage.setItem('tc_source_type', obSourceType);
      sessionStorage.setItem('tc_scan_data', JSON.stringify(combined));
      obShowSuccess(sources[0].url, combined);"""

content = content.replace(old_show, new_show)
print('Fix1:', 'will be overridden' in content)
print('Fix2:', 'Save AFTER obCombineScores' in content)

with open('dashboard.html', 'w') as f:
    f.write(content)
