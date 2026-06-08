with open('dashboard.html', 'r') as f:
    content = f.read()

# Find the reset block and move it to run FIRST
reset_start = content.find('// ── RESET ONBOARDING VIA URL PARAM ──')
reset_end = content.find('})();', reset_start) + 5
reset_block = content[reset_start:reset_end]

# Remove from current location
content = content.replace(reset_block, '')

# Add at the very start of the first script tag
first_script = content.find('<script>')
content = content[:first_script + 8] + '\n' + reset_block + '\n' + content[first_script + 8:]

print('Reset moved to top:', content.find(reset_block) < content.find('function obInit'))
with open('dashboard.html', 'w') as f:
    f.write(content)
