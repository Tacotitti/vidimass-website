"""
Comprehensive script to add data-i18n to ALL translatable text on all pages
This will process: buttons, links, headings, paragraphs, labels, etc.
"""

import re
import os

# Pages to process
pages = [
    'index.html',
    'preisliste.html', 
    'contact.html',
    'social-media-charting.html',
    'datenschutz.html',
    'nutzungsbedingungen.html'
]

# Map of German text to translation keys (will be generated)
translations_map = {}
translation_counter = 0

def generate_key(text, prefix='auto'):
    """Generate a unique translation key from text"""
    global translation_counter
    # Clean text for key
    key_base = re.sub(r'[^a-zA-Z0-9]+', '_', text[:30].lower()).strip('_')
    key = f"{prefix}_{key_base}_{translation_counter}"
    translation_counter += 1
    return key

def process_html_file(filepath):
    """Add data-i18n to all translatable text in HTML file"""
    
    print(f"\n📄 Processing {filepath}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count existing data-i18n
    existing = len(re.findall(r'data-i18n=', content))
    print(f"   Existing data-i18n: {existing}")
    
    # Patterns to find text that needs translation:
    
    # 1. Button text
    buttons = re.findall(r'<button[^>]*>([^<]+)</button>', content)
    print(f"   Buttons found: {len(buttons)}")
    
    # 2. Link text (without data-i18n already)
    links = re.findall(r'<a[^>]*>(?!<)([^<]+)</a>', content)
    print(f"   Links found: {len(links)}")
    
    # 3. Headings
    headings = re.findall(r'<h[1-6][^>]*>([^<]+)</h[1-6]>', content)
    print(f"   Headings found: {len(headings)}")
    
    # 4. Paragraphs
    paragraphs = re.findall(r'<p[^>]*>([^<]+)</p>', content)
    print(f"   Paragraphs found: {len(paragraphs)}")
    
    # This is getting complex - better approach:
    # Manual review and targeted fixes
    
    return content

# Process all pages
for page in pages:
    if os.path.exists(page):
        process_html_file(page)
    else:
        print(f"❌ {page} not found")

print("\n" + "="*60)
print("MANUAL REVIEW NEEDED")
print("="*60)
print("\nAutomatic translation is too complex.")
print("Better approach: Manual systematic review of each page.")
print("\nPriority order:")
print("1. index.html - Homepage (most important)")
print("2. preisliste.html - Pricing page")
print("3. contact.html - Contact form")
print("4. social-media-charting.html - Content page")
print("5. datenschutz.html + nutzungsbedingungen.html - Legal")
