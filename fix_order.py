with open('dashboard.html', 'r') as f:
    content = f.read()

# Find detectUrlType function
detect_start = content.find('function detectUrlType(url) {')
detect_end = content.find('\n}', detect_start) + 2
detect_fn = content[detect_start:detect_end]

# Remove from current location
content = content.replace(detect_fn + '\n', '')

# Insert BEFORE obInit
obinit_pos = content.find('function obInit() {')
content = content[:obinit_pos] + detect_fn + '\n\n' + content[obinit_pos:]

print('detectUrlType before obInit:', content.find('function detectUrlType') < content.find('function obInit'))
with open('dashboard.html', 'w') as f:
    f.write(content)
