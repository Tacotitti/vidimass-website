"""
AUTOMATIC WEBSITE TRANSLATION SYSTEM
Using DeepL API to translate ALL German text to 8 languages

Process:
1. Scan all HTML files for German text
2. Extract text + generate unique keys
3. Translate to EN, TR, PT, ES, RU, ZH, AR using DeepL
4. Add data-i18n attributes to HTML
5. Update translations.js with all translations
"""

import requests
import re
import json
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment (NEVER hardcode API keys!)
DEEPL_API_KEY = os.getenv('DEEPL_API_KEY')
if not DEEPL_API_KEY:
    raise ValueError("DEEPL_API_KEY not found! Create .env file with your API key.")

# Language mapping for DeepL
DEEPL_LANGS = {
    'en': 'EN',      # English
    'tr': 'TR',      # Turkish
    'pt': 'PT-PT',   # Portuguese
    'es': 'ES',      # Spanish
    'ru': 'RU',      # Russian
    'zh': 'ZH',      # Chinese
    'ar': 'AR'       # Arabic
}

def translate_text(text, target_lang):
    """Translate text using DeepL API"""
    url = "https://api.deepl.com/v2/translate"
    
    headers = {
        "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "text": [text],
        "source_lang": "DE",
        "target_lang": target_lang
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            return result['translations'][0]['text']
        else:
            print(f"  Error translating to {target_lang}: {response.status_code}")
            return None
    except Exception as e:
        print(f"  Exception: {e}")
        return None

def extract_german_texts(html_file):
    """Extract all German text from HTML that needs translation"""
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    texts_to_translate = []
    
    # German indicators
    german_patterns = [r'\bfür\b', r'\bund\b', r'\boder\b', r'\bmit\b', r'ä', r'ö', r'ü', r'ß']
    
    # Check title
    title = soup.find('title')
    if title and not title.has_attr('data-i18n'):
        text = title.get_text(strip=True)
        if any(re.search(p, text, re.IGNORECASE) for p in german_patterns):
            texts_to_translate.append({
                'element': 'title',
                'text': text,
                'context': html_file
            })
    
    # Check all text elements
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'span', 'div', 'label', 'button', 'a', 'li']):
        # Skip if already has translation
        if tag.has_attr('data-i18n') or tag.has_attr('data-i18n-html'):
            continue
        
        # Get direct text only (not children)
        text = ''.join(tag.find_all(text=True, recursive=False)).strip()
        if not text or len(text) < 5:
            continue
        
        # Check if German
        if any(re.search(p, text, re.IGNORECASE) for p in german_patterns):
            texts_to_translate.append({
                'element': tag.name,
                'text': text,
                'context': f"{html_file} - {tag.get('class', [''])[0] if tag.get('class') else 'no-class'}"
            })
    
    return texts_to_translate

# TEST: Extract from index.html
print("="*60)
print("STEP 1: Extract German texts from index.html")
print("="*60)

texts = extract_german_texts('index.html')
print(f"\nFound {len(texts)} German texts to translate")

# Show first 10
print("\nFirst 10 texts:")
for i, item in enumerate(texts[:10], 1):
    print(f"{i}. [{item['element']}] {item['text'][:60]}...")

# TEST: Translate one text to all languages
if texts:
    print("\n" + "="*60)
    print("STEP 2: Test translation to all languages")
    print("="*60)
    
    test_text = texts[0]['text']
    print(f"\nOriginal (DE): {test_text}\n")
    
    translations = {'de': test_text}
    
    for lang_code, deepl_lang in DEEPL_LANGS.items():
        print(f"Translating to {lang_code.upper()}...", end=" ")
        translation = translate_text(test_text, deepl_lang)
        if translation:
            translations[lang_code] = translation
            print(f"OK: {translation[:50]}...")
        else:
            print("FAILED")
        time.sleep(0.5)  # Rate limiting
    
    print("\n" + "="*60)
    print("TRANSLATION TEST COMPLETE")
    print("="*60)
    print("\nAll translations:")
    for lang, trans in translations.items():
        print(f"  {lang.upper()}: {trans}")

print("\n✅ System is ready!")
print("\nNext: Run full automatic translation for all pages")
