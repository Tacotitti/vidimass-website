"""
AUTOMATIC TRANSLATION SYSTEM with DeepL API
Step 1: Test the API key and translate a sample text
"""

import requests
import json

DEEPL_API_KEY = "47c6210a-e21d-4b9b-856a-06ad267eedb4"  # Try without suffix first

def test_deepl_api():
    """Test if DeepL API key works"""
    url = "https://api.deepl.com/v2/translate"
    
    headers = {
        "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "text": ["Mass Posting für TikTok, Instagram & Spotify Charting"],
        "source_lang": "DE",
        "target_lang": "EN"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            translated = result['translations'][0]['text']
            print(f"\nOK DeepL API works!")
            print(f"Original (DE): {data['text'][0]}")
            print(f"Translated (EN): {translated}")
            return True
        else:
            print("\nAPI Error - Status:", response.status_code)
            print("Response:", response.text[:200])
            return False
            
    except Exception as e:
        print("\nException:", str(e))
        return False

def get_usage():
    """Check API usage limits"""
    url = "https://api.deepl.com/v2/usage"
    
    headers = {
        "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            usage = response.json()
            character_count = usage.get('character_count', 0)
            character_limit = usage.get('character_limit', 0)
            remaining = character_limit - character_count
            
            print(f"\nAPI Usage:")
            print(f"   Used: {character_count:,} characters")
            print(f"   Limit: {character_limit:,} characters")
            print(f"   Remaining: {remaining:,} characters")
            print(f"   Percentage used: {(character_count/character_limit*100):.1f}%")
            return True
        else:
            print(f"Could not get usage: {response.text}")
            return False
    except Exception as e:
        print(f"Exception: {e}")
        return False

# Test the API
print("="*60)
print("DEEPL API TEST")
print("="*60)

if test_deepl_api():
    get_usage()
    print("\n✅ API is ready to use!")
    print("\nNext steps:")
    print("1. Extract all German text from HTML files")
    print("2. Translate to EN, TR, PT, ES, RU, ZH, AR")
    print("3. Add data-i18n attributes automatically")
    print("4. Update translations.js")
else:
    print("\n❌ API test failed. Check the key.")
