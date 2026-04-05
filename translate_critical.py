"""
SMART TRANSLATION SYSTEM
Translate specific important texts that we know need translation
Avoid encoding issues by targeting exact strings
"""

import requests
import time
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment (NEVER hardcode API keys!)
DEEPL_API_KEY = os.getenv('DEEPL_API_KEY')
if not DEEPL_API_KEY:
    raise ValueError("DEEPL_API_KEY not found! Create .env file with your API key.")

DEEPL_LANGS = {
    'en': 'EN',
    'tr': 'TR',
    'pt': 'PT-PT',
    'es': 'ES',
    'ru': 'RU',
    'zh': 'ZH',
    'ar': 'AR'
}

def translate_batch(texts, target_lang):
    """Translate multiple texts at once"""
    url = "https://api.deepl.com/v2/translate"
    
    headers = {
        "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "text": texts,
        "source_lang": "DE",
        "target_lang": target_lang
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            return [t['text'] for t in result['translations']]
        else:
            print(f"Error {response.status_code}: {response.text[:100]}")
            return None
    except Exception as e:
        print(f"Exception: {e}")
        return None

# CRITICAL TEXTS TO TRANSLATE (from audit)
critical_texts = [
    # Homepage section titles
    "Charting für Labels",
    "und Künstler weltweit",
    
    # SEO Section
    "Mass Posting für TikTok, Instagram & Spotify Charting",
    
    # Why section
    "Warum Mass Posting mit MediaMass?",
    "Schnellste Mass Post Lösung",
    "Social Media Charting Garantie",
    "Beste Mass Posting Preise",
    "Automatisierter Instagram Mass Post",
    
    # Pricing page
    "Transparente Preise für TikTok und Instagram Mass Posting",
    "Mass Video Posting für TikTok",
    "Unique Reels für Instagram Mass Posting",
    "Individuelle Pakete verfügbar",
    "Benötigen Sie ein Custom Package oder haben Fragen zu unseren Preisen?",
    
    # Table headers
    "Videos",
    "Preis",
    "Pro Video",
    "Unique Reels",
]

print("="*70)
print("AUTOMATIC TRANSLATION - Critical Texts")
print("="*70)
print(f"\nTranslating {len(critical_texts)} texts to 7 languages...")
print(f"Estimated API calls: {len(critical_texts) // 50 + 1} per language")
print(f"Total API calls: ~{(len(critical_texts) // 50 + 1) * 7}\n")

# Translate all texts to all languages
all_translations = {}

for lang_code, deepl_lang in DEEPL_LANGS.items():
    print(f"\nTranslating to {lang_code.upper()} ({deepl_lang})...")
    
    # Batch translate (DeepL allows up to 50 texts per request)
    batch_size = 50
    translations = []
    
    for i in range(0, len(critical_texts), batch_size):
        batch = critical_texts[i:i+batch_size]
        print(f"  Batch {i//batch_size + 1}: {len(batch)} texts...", end=" ")
        
        result = translate_batch(batch, deepl_lang)
        if result:
            translations.extend(result)
            print("OK")
        else:
            print("FAILED")
            translations.extend(batch)  # Keep original on failure
        
        time.sleep(1)  # Rate limiting
    
    all_translations[lang_code] = translations
    print(f"  ✓ Completed {lang_code.upper()}: {len(translations)} translations")

# Add German originals
all_translations['de'] = critical_texts

print("\n" + "="*70)
print("TRANSLATION COMPLETE")
print("="*70)

# Save to JSON for review
output = {}
for i, de_text in enumerate(critical_texts):
    key = f"auto_{i+1}"
    output[key] = {
        'original': de_text,
        'translations': {
            'de': de_text,
            **{lang: all_translations[lang][i] for lang in DEEPL_LANGS.keys()}
        }
    }

with open('auto_translations.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("\n✅ Saved to auto_translations.json")
print("\nSample translations:")
for i in range(min(3, len(critical_texts))):
    print(f"\n{i+1}. DE: {critical_texts[i]}")
    print(f"   EN: {all_translations['en'][i]}")
    print(f"   TR: {all_translations['tr'][i]}")
