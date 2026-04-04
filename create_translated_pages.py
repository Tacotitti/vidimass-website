"""
Create fully translated HTML pages using translations.js
Generates: index-de.html, index-tr.html, etc. for all languages
"""

import re
import json

# Read translations.js and parse it
with open('translations.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Extract translation objects for each language
# Format: const translations = { en: { ... }, de: { ... }, ... }

def extract_translations():
    """Parse translations.js and extract all language objects"""
    translations = {}
    
    # Find each language block
    lang_pattern = r"(\w+):\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\},"
    
    # Simplified: manually map the translations we have
    translations = {
        'en': {},
        'de': {},
        'tr': {},
        'pt': {},
        'es': {},
        'ru': {},
        'zh': {},
        'ar': {}
    }
    
    # Parse each language section
    current_lang = None
    in_lang_block = False
    
    for line in js_content.split('\n'):
        # Detect language start
        if re.match(r'\s*(en|de|tr|pt|es|ru|zh|ar):\s*\{', line):
            current_lang = re.match(r'\s*(\w+):', line).group(1)
            in_lang_block = True
            continue
        
        # Detect end of language block
        if in_lang_block and line.strip().startswith('},'):
            in_lang_block = False
            current_lang = None
            continue
        
        # Extract key-value pairs
        if in_lang_block and current_lang and ':' in line:
            match = re.search(r'(\w+):\s*"([^"]*)"', line)
            if match:
                key = match.group(1)
                value = match.group(2)
                translations[current_lang][key] = value
    
    return translations

def translate_html(html_content, lang_code, translations):
    """Replace all data-i18n elements with translated text"""
    
    lang_trans = translations.get(lang_code, {})
    
    # 1. Update <html lang="">
    html_content = re.sub(r'<html lang="[^"]*">', f'<html lang="{lang_code}">', html_content)
    
    # 2. Replace elements with data-i18n
    def replace_i18n(match):
        full_match = match.group(0)
        key = match.group(1)
        translated = lang_trans.get(key, f"[{key}]")
        
        # Replace the inner text between tags
        # Pattern: <tag data-i18n="key">OLD TEXT</tag>
        result = re.sub(r'>([^<]*)</\w+>$', f'>{translated}</\\g<1>>', full_match)
        
        # Remove data-i18n attribute
        result = re.sub(r'\s*data-i18n="[^"]*"', '', result)
        
        return result
    
    # Find all elements with data-i18n
    html_content = re.sub(
        r'<(\w+)[^>]*data-i18n="([^"]*)"[^>]*>.*?</\1>',
        replace_i18n,
        html_content,
        flags=re.DOTALL
    )
    
    # 3. Translate common static text (hardcoded)
    if lang_code == 'de':
        html_content = html_content.replace('Social Media Charting', 'Social Media Charting')
        html_content = html_content.replace('Preisliste', 'Preisliste')
        html_content = html_content.replace('Kontakt', 'Kontakt')
    
    # 4. Remove language.js and translations.js (not needed anymore)
    html_content = re.sub(r'<script src="language\.js"></script>\s*', '', html_content)
    html_content = re.sub(r'<script src="translations\.js"></script>\s*', '', html_content)
    
    return html_content

print("📖 Parsing translations.js...")
translations = extract_translations()

print(f"✓ Loaded {len(translations)} languages")
for lang in translations:
    print(f"  {lang}: {len(translations[lang])} keys")

print("\n🔄 Creating translated HTML files...")

# Pages to translate
PAGES = ['index.html', 'preisliste.html', 'contact.html', 'social-media-charting.html', 
         'datenschutz.html', 'nutzungsbedingungen.html']

for page in PAGES:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            original_html = f.read()
        
        print(f"\n📄 {page}")
        
        for lang_code in ['en', 'de', 'tr', 'pt', 'es', 'ru', 'zh', 'ar']:
            translated_html = translate_html(original_html, lang_code, translations)
            
            output_file = page.replace('.html', f'-{lang_code}.html')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(translated_html)
            
            print(f"  ✓ {lang_code}: {output_file}")
    
    except FileNotFoundError:
        print(f"  ❌ {page} not found")

print("\n✅ Translation complete!")
print("📦 Created translated HTML files for all languages")
