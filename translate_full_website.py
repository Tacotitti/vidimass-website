"""
Create fully translated versions of all HTML pages for each language.
This will generate separate HTML files like: index-de.html, index-tr.html, etc.
"""

import os
import re
from deep_translator import GoogleTranslator

# Language configurations
LANGUAGES = {
    'en': {'name': 'English', 'flag': '🇬🇧'},
    'de': {'name': 'Deutsch', 'flag': '🇩🇪'},
    'tr': {'name': 'Türkçe', 'flag': '🇹🇷'},
    'pt': {'name': 'Português', 'flag': '🇵🇹'},
    'es': {'name': 'Español', 'flag': '🇪🇸'},
    'ru': {'name': 'Русский', 'flag': '🇷🇺'},
    'zh': {'name': '中文', 'flag': '🇨🇳'},
    'ar': {'name': 'العربية', 'flag': '🇸🇦'}
}

# HTML pages to translate
PAGES = [
    'index.html',
    'preisliste.html',
    'contact.html',
    'social-media-charting.html',
    'datenschutz.html',
    'nutzungsbedingungen.html'
]

# Elements to NOT translate (keep original)
SKIP_TRANSLATE = [
    'MediaMass',
    'TikTok',
    'Instagram',
    'Spotify',
    'Apple Music',
    'Shazam',
    'info@masspost.store',
    '@sennaook',
    'masspost.store',
    'script.js',
    'language.js',
    'translations.js',
    'styles.css',
    'logo.png',
    'telegram-qr.png'
]

def translate_text(text, target_lang):
    """Translate text to target language using Google Translate"""
    if not text or not text.strip():
        return text
    
    # Skip if contains only numbers, symbols, or skip words
    if any(skip in text for skip in SKIP_TRANSLATE):
        return text
    
    try:
        translator = GoogleTranslator(source='auto', target=target_lang)
        translated = translator.translate(text)
        return translated
    except Exception as e:
        print(f"  ⚠️  Translation error: {e}")
        return text

def translate_html_content(html_content, target_lang):
    """Translate all visible text in HTML while preserving structure"""
    
    # Patterns to find translatable text
    # 1. Text between tags
    def replace_tag_text(match):
        full_match = match.group(0)
        text = match.group(1)
        if text.strip():
            translated = translate_text(text, target_lang)
            return full_match.replace(text, translated)
        return full_match
    
    # Translate text between HTML tags
    html_content = re.sub(r'>([^<]+)<', replace_tag_text, html_content)
    
    # 2. Translate placeholder attributes
    def replace_placeholder(match):
        attr = match.group(0)
        text = match.group(1)
        translated = translate_text(text, target_lang)
        return attr.replace(text, translated)
    
    html_content = re.sub(r'placeholder="([^"]+)"', replace_placeholder, html_content)
    
    # 3. Translate title attributes
    html_content = re.sub(r'title="([^"]+)"', replace_placeholder, html_content)
    
    # 4. Translate alt attributes
    html_content = re.sub(r'alt="([^"]+)"', replace_placeholder, html_content)
    
    # 5. Update lang attribute
    html_content = re.sub(r'<html lang="[^"]*">', f'<html lang="{target_lang}">', html_content)
    
    return html_content

def create_translated_pages():
    """Create fully translated HTML files for each language"""
    
    for page in PAGES:
        if not os.path.exists(page):
            print(f"❌ Skip {page} (not found)")
            continue
        
        print(f"\n📄 Processing {page}...")
        
        with open(page, 'r', encoding='utf-8') as f:
            original_html = f.read()
        
        for lang_code, lang_info in LANGUAGES.items():
            if lang_code == 'en':
                # English is the original, just copy
                output_file = page.replace('.html', '-en.html')
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(original_html)
                print(f"  ✓ {lang_info['flag']} {lang_info['name']}: {output_file} (original)")
                continue
            
            print(f"  🔄 Translating to {lang_info['flag']} {lang_info['name']}...")
            
            # Translate HTML
            translated_html = translate_html_content(original_html, lang_code)
            
            # Save translated file
            output_file = page.replace('.html', f'-{lang_code}.html')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(translated_html)
            
            print(f"  ✓ {lang_info['flag']} {lang_info['name']}: {output_file}")
    
    print("\n✅ All pages translated!")
    print(f"📦 Created {len(PAGES) * len(LANGUAGES)} files")

if __name__ == '__main__':
    print("🌍 Starting full website translation...")
    print(f"📄 Pages: {len(PAGES)}")
    print(f"🌐 Languages: {len(LANGUAGES)}")
    print()
    create_translated_pages()
