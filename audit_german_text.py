"""
Comprehensive audit: Find ALL German text that needs English translation
Checks ALL 6 pages for untranslated content
"""

from bs4 import BeautifulSoup
import re

pages = {
    'index.html': 'Homepage',
    'preisliste.html': 'Pricing Page',
    'contact.html': 'Contact Page',
    'social-media-charting.html': 'Social Media Charting',
    'datenschutz.html': 'Privacy Policy',
    'nutzungsbedingungen.html': 'Terms of Service'
}

# German-specific patterns to detect
german_indicators = [
    r'\bund\b', r'\bfür\b', r'\boder\b', r'\bmit\b', r'\bauf\b',
    r'\büber\b', r'\bvon\b', r'\bzu\b', r'\bin\b', r'\bist\b',
    r'\bSie\b', r'\bIhr\b', r'\bwir\b', r'\bWir\b',
    r'ä', r'ö', r'ü', r'ß', r'Ä', r'Ö', r'Ü'
]

print("=" * 80)
print("COMPLETE GERMAN TEXT AUDIT - ALL PAGES")
print("=" * 80)

for filename, pagename in pages.items():
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()
        
        soup = BeautifulSoup(html, 'html.parser')
        
        print(f"\n{'='*80}")
        print(f"📄 {pagename} ({filename})")
        print('='*80)
        
        # Check title
        title = soup.find('title')
        if title:
            text = title.get_text()
            has_data_i18n = title.has_attr('data-i18n')
            if any(re.search(pattern, text, re.IGNORECASE) for pattern in german_indicators):
                status = "✅" if has_data_i18n else "❌"
                print(f"\n{status} TITLE: {text}")
                if not has_data_i18n:
                    print(f"   → Missing data-i18n attribute!")
        
        # Check all visible text elements
        for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'span', 'div', 'label', 'button', 'a', 'li', 'option']):
            # Skip script/style content
            if tag.parent.name in ['script', 'style']:
                continue
            
            text = tag.get_text(strip=True)
            if not text or len(text) < 3:
                continue
            
            # Check if it contains German
            if any(re.search(pattern, text, re.IGNORECASE) for pattern in german_indicators):
                # Check if it has translation attribute
                has_i18n = (tag.has_attr('data-i18n') or 
                           tag.has_attr('data-i18n-html') or
                           tag.has_attr('data-i18n-placeholder') or
                           tag.parent.has_attr('data-i18n') or
                           tag.parent.has_attr('data-i18n-html'))
                
                status = "✅" if has_i18n else "❌"
                
                # Only show untranslated (missing data-i18n)
                if not has_i18n:
                    print(f"\n{status} <{tag.name}>: {text[:80]}")
                    if tag.has_attr('class'):
                        print(f"   Class: {' '.join(tag['class'])}")
        
        # Check placeholders
        for input_tag in soup.find_all(['input', 'textarea']):
            if input_tag.has_attr('placeholder'):
                placeholder = input_tag['placeholder']
                if any(re.search(pattern, placeholder, re.IGNORECASE) for pattern in german_indicators):
                    has_i18n = input_tag.has_attr('data-i18n-placeholder')
                    status = "✅" if has_i18n else "❌"
                    if not has_i18n:
                        print(f"\n{status} PLACEHOLDER: {placeholder}")
                        print(f"   Element: <{input_tag.name} id={input_tag.get('id', 'N/A')}>")
    
    except FileNotFoundError:
        print(f"\n❌ File not found: {filename}")
    except Exception as e:
        print(f"\n❌ Error processing {filename}: {e}")

print("\n" + "="*80)
print("AUDIT COMPLETE")
print("="*80)
print("\nLegend:")
print("✅ = Has translation markup (data-i18n)")
print("❌ = Missing translation markup (needs to be added)")
