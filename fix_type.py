with open('dashboard.html', 'r') as f:
    content = f.read()

old = "function obCombineScores(results) {\n  if (results.length === 1) return results[0].data;"
new = """function obCombineScores(results) {
  if (results.length === 1) {
    var d = results[0].data;
    d.creator_type = results[0].source.type;
    obSourceType = results[0].source.type;
    return d;
  }"""
content = content.replace(old, new)

old2 = "  obSourceType = sources[0].type;\n\n  // Show scanning step"
new2 = "  obSourceType = sources[0].type;\n  sessionStorage.setItem('tc_source_type', obSourceType);\n\n  // Show scanning step"
content = content.replace(old2, new2)

with open('dashboard.html', 'w') as f:
    f.write(content)
print('Fix1:', 'obSourceType = results[0].source.type' in content)
print('Fix2:', "setItem('tc_source_type'" in content)
