import os
import re

# 1. Rename file
if os.path.exists('tiktok-charting.html'):
    os.rename('tiktok-charting.html', 'social-media-charting.html')
    print("✓ Renamed: tiktok-charting.html → social-media-charting.html")

# 2. Update all HTML files
html_files = [
    'index.html',
    'social-media-charting.html',
    'preisliste.html',
    'contact.html',
    'datenschutz.html',
    'nutzungsbedingungen.html'
]

for file in html_files:
    if not os.path.exists(file):
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace file links
    content = content.replace('tiktok-charting.html', 'social-media-charting.html')
    
    # Replace text "TikTok Charting" with "Social Media Charting"
    content = content.replace('TikTok Charting', 'Social Media Charting')
    
    # Update page title if it's the charting page itself
    if file == 'social-media-charting.html':
        content = re.sub(
            r'<title>.*?</title>',
            '<title>Social Media Charting - TikTok & Instagram Algorithm | MediaMass</title>',
            content
        )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated: {file}")

# 3. Update script.js (mobile menu)
if os.path.exists('script.js'):
    with open('script.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('tiktok-charting.html', 'social-media-charting.html')
    content = content.replace('TikTok Charting', 'Social Media Charting')
    
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Updated: script.js")

print("\n✅ Done - All references updated to 'Social Media Charting'")
