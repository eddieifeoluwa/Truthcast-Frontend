with open('dashboard.html', 'r') as f:
    content = f.read()

# Find and fix the populateDashboard section that sets tc_onboarded
# It should NOT set tc_onboarded - only obInit should do that
old = """        // Has scan data → mark onboarded and wire
        sessionStorage.setItem('tc_onboarded', 'true');
        try {
          obScanData = JSON.parse(scanData);
          setTimeout(obWireDashboard, 300);
        } catch(e){}"""

new = """        // Has scan data → wire dashboard (don't set onboarded here)
        try {
          obScanData = JSON.parse(scanData);
          setTimeout(obWireDashboard, 300);
        } catch(e){}"""

result = content.replace(old, new)
print('Fix1:', result != content)

# Also fix the other tc_onboarded set in populateDashboard
old2 = """    // Clear any previous user's scan data so new user gets fresh onboarding
    sessionStorage.removeItem('tc_onboarded');"""

new2 = """    // Always clear onboarded flag - let obInit decide
    sessionStorage.removeItem('tc_onboarded');"""

result = result.replace(old2, new2)

with open('dashboard.html', 'w') as f:
    f.write(result)
print('Saved')
