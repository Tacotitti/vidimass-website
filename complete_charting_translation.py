#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete Translation System for Social Media Charting Page
Extracts ALL text, translates via DeepL, updates HTML and translations.js
"""

import os
import re
import json
import requests
import sys
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from typing import Dict, List, Tuple
import time

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Load DeepL API key
load_dotenv()
DEEPL_API_KEY = os.getenv('DEEPL_API_KEY')
if not DEEPL_API_KEY:
    raise ValueError("DEEPL_API_KEY not found in .env file!")

DEEPL_URL = "https://api.deepl.com/v2/translate"

# File paths
HTML_FILE = "social-media-charting.html"
TRANSLATIONS_FILE = "translations.js"

# Target languages
TARGET_LANGUAGES = {
    'EN': 'en',
    'TR': 'tr',
    'PT-PT': 'pt',
    'ES': 'es'
}

def extract_german_texts_from_html(html_path: str) -> Dict[str, str]:
    """
    Extract all German text that has data-i18n attributes
    Returns: {translation_key: german_text}
    """
    print("Scanning HTML for text with data-i18n attributes...")
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    texts = {}
    
    # Find all elements with data-i18n
    for elem in soup.find_all(attrs={'data-i18n': True}):
        key = elem.get('data-i18n')
        text = elem.get_text(strip=True)
        if text and key:
            texts[key] = text
    
    # Find all elements with data-i18n-html
    for elem in soup.find_all(attrs={'data-i18n-html': True}):
        key = elem.get('data-i18n-html')
        # Get inner HTML
        inner_html = elem.decode_contents().strip()
        if inner_html and key:
            texts[key] = inner_html
    
    print(f"Found {len(texts)} translation keys with data-i18n")
    return texts

def clean_html_for_translation(html_text: str) -> str:
    """Remove HTML tags for translation, preserving placeholders"""
    # Replace <strong> tags with placeholders
    text = re.sub(r'<strong[^>]*>(.*?)</strong>', r'[[STRONG]]\1[[/STRONG]]', html_text)
    text = re.sub(r'<em[^>]*>(.*?)</em>', r'[[EM]]\1[[/EM]]', html_text)
    text = re.sub(r'<code[^>]*>(.*?)</code>', r'[[CODE]]\1[[/CODE]]', html_text)
    # Remove remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Clean whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def restore_html_tags(translated_text: str) -> str:
    """Restore HTML tags after translation"""
    text = re.sub(r'\[\[STRONG\]\](.*?)\[\[/STRONG\]\]', r'<strong class="text-white">\1</strong>', translated_text)
    text = re.sub(r'\[\[EM\]\](.*?)\[\[/EM\]\]', r'<em>\1</em>', translated_text)
    text = re.sub(r'\[\[CODE\]\](.*?)\[\[/CODE\]\]', r'<code class="text-cyan-400 bg-slate-900/50 px-3 py-1 rounded mt-2 inline-block">\1</code>', translated_text)
    return text

def translate_via_deepl(texts: Dict[str, str], target_lang: str) -> Dict[str, str]:
    """
    Translate texts via DeepL API (batch mode, max 50 per call)
    """
    print(f"Translating {len(texts)} texts to {target_lang}...")
    
    translations = {}
    text_items = list(texts.items())
    batch_size = 50
    
    for i in range(0, len(text_items), batch_size):
        batch = text_items[i:i+batch_size]
        keys = [item[0] for item in batch]
        source_texts = [item[1] for item in batch]
        
        # Clean HTML tags for translation
        clean_texts = [clean_html_for_translation(text) for text in source_texts]
        
        try:
            response = requests.post(
                DEEPL_URL,
                headers={
                    'Authorization': f'DeepL-Auth-Key {DEEPL_API_KEY}',
                    'Content-Type': 'application/json'
                },
                json={
                    'text': clean_texts,
                    'target_lang': target_lang,
                    'source_lang': 'DE'
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                for idx, translation_obj in enumerate(result['translations']):
                    translated = translation_obj['text']
                    # Restore HTML tags if original had them
                    if '[[' in translated:
                        translated = restore_html_tags(translated)
                    translations[keys[idx]] = translated
                print(f"  Batch {i//batch_size + 1}/{(len(text_items)-1)//batch_size + 1} complete")
            else:
                print(f"  DeepL API error: {response.status_code}")
                print(f"  Response: {response.text}")
                # Fallback: use original text
                for idx, key in enumerate(keys):
                    translations[key] = source_texts[idx]
            
            # Rate limiting
            time.sleep(0.5)
        
        except Exception as e:
            print(f"  Translation error: {e}")
            # Fallback
            for idx, key in enumerate(keys):
                translations[key] = source_texts[idx]
    
    print(f"  {target_lang} translation complete!")
    return translations

def read_existing_translations() -> Dict[str, Dict[str, str]]:
    """Read existing translations from translations.js"""
    print("Reading existing translations.js...")
    
    with open(TRANSLATIONS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse the JavaScript object (simplified parsing)
    translations = {'en': {}, 'de': {}, 'tr': {}, 'pt': {}, 'es': {}}
    
    # Extract each language block
    for lang in ['en', 'de', 'tr', 'pt', 'es']:
        pattern = rf'{lang}:\s*\{{([^}}]+(?:\}}[^}}]+)*?)\}},'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            block = match.group(1)
            # Extract key-value pairs
            for line in block.split('\n'):
                # Match: key: "value",
                kv_match = re.match(r'\s*([a-zA-Z_0-9]+):\s*"((?:[^"\\]|\\.)*)",?', line)
                if kv_match:
                    key = kv_match.group(1)
                    value = kv_match.group(2)
                    # Unescape
                    value = value.replace('\\"', '"').replace('\\n', '\n')
                    translations[lang][key] = value
    
    total = sum(len(v) for v in translations.values())
    print(f"Found {total} existing translation entries")
    return translations

def merge_translations(existing: Dict[str, Dict[str, str]], new_de: Dict[str, str], new_translations: Dict[str, Dict[str, str]]) -> Dict[str, Dict[str, str]]:
    """Merge new translations with existing ones"""
    print("Merging translations...")
    
    # Add German texts
    for key, text in new_de.items():
        existing['de'][key] = text
    
    # Add translations for other languages
    for lang in ['en', 'tr', 'pt', 'es']:
        if lang in new_translations:
            for key, text in new_translations[lang].items():
                existing[lang][key] = text
    
    return existing

def write_translations_js(translations: Dict[str, Dict[str, str]]):
    """Write updated translations to translations.js"""
    print("Writing updated translations.js...")
    
    # Read original file to preserve structure
    with open(TRANSLATIONS_FILE, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # For each language, update its section
    new_content = original_content
    
    for lang in ['en', 'de', 'tr', 'pt', 'es']:
        # Build the new language object
        entries = []
        for key in sorted(translations[lang].keys()):
            value = translations[lang][key]
            # Escape for JavaScript string
            escaped = value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
            entries.append(f'        {key}: "{escaped}"')
        
        new_lang_block = ',\n'.join(entries)
        
        # Replace the language block in the file
        pattern = rf'({lang}:\s*\{{)([^}}]+(?:\}}[^}}]+)*?)(\}},?)'
        replacement = rf'\1\n{new_lang_block}\n    \3'
        new_content = re.sub(pattern, replacement, new_content, flags=re.DOTALL)
    
    # Write the file
    with open(TRANSLATIONS_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("translations.js updated successfully!")

def main():
    """Main execution"""
    print("=" * 60)
    print("COMPLETE SOCIAL MEDIA CHARTING PAGE TRANSLATION")
    print("=" * 60)
    print()
    
    # Step 1: Extract German texts from HTML
    german_texts = extract_german_texts_from_html(HTML_FILE)
    print(f"Extracted {len(german_texts)} text elements")
    print()
    
    # Step 2: Read existing translations
    existing_translations = read_existing_translations()
    print()
    
    # Step 3: Identify what needs translation
    keys_to_translate = []
    for key in german_texts.keys():
        needs_translation = False
        for lang in ['en', 'tr', 'pt', 'es']:
            if key not in existing_translations[lang]:
                needs_translation = True
                break
        if needs_translation:
            keys_to_translate.append(key)
    
    print(f"{len(keys_to_translate)} keys need translation")
    print()
    
    # Step 4: Translate missing keys
    new_translations = {}
    if keys_to_translate:
        texts_to_translate = {k: german_texts[k] for k in keys_to_translate}
        
        for deepl_code, lang_code in TARGET_LANGUAGES.items():
            print(f"Translating to {lang_code.upper()}...")
            translations = translate_via_deepl(texts_to_translate, deepl_code)
            new_translations[lang_code] = translations
            print()
    
    # Step 5: Merge and write translations
    merged = merge_translations(existing_translations, german_texts, new_translations)
    write_translations_js(merged)
    
    # Report
    print()
    print("=" * 60)
    print("TRANSLATION COMPLETE!")
    print("=" * 60)
    print(f"Total translation keys: {len(german_texts)}")
    print(f"New keys translated: {len(keys_to_translate)}")
    print(f"Languages: EN, DE, TR, PT, ES (5 languages)")
    print()
    print("Summary:")
    for lang in ['en', 'de', 'tr', 'pt', 'es']:
        print(f"  {lang.upper()}: {len(merged[lang])} translations")
    print()
    print("All files updated successfully!")

if __name__ == '__main__':
    main()
