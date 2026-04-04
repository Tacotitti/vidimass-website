"""Add nav_charting and nav_pricing to all language blocks in translations.js"""

translations_to_add = {
    'en': {
        'nav_charting': 'Social Media Charting',
        'nav_pricing': 'Pricing'
    },
    'de': {
        'nav_charting': 'Social Media Charting',
        'nav_pricing': 'Preisliste'
    },
    'tr': {
        'nav_charting': 'Sosyal Medya Charting',
        'nav_pricing': 'Fiyatlandırma'
    },
    'pt': {
        'nav_charting': 'Social Media Charting',
        'nav_pricing': 'Preços'
    },
    'es': {
        'nav_charting': 'Social Media Charting',
        'nav_pricing': 'Precios'
    },
    'ru': {
        'nav_charting': 'Social Media Charting',
        'nav_pricing': 'Цены'
    },
    'zh': {
        'nav_charting': '社交媒体排行',
        'nav_pricing': '价格'
    },
    'ar': {
        'nav_charting': 'تصنيف وسائل التواصل الاجتماعي',
        'nav_pricing': 'الأسعار'
    }
}

with open('translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the new keys after nav_get_started in each language block
for lang, trans in translations_to_add.items():
    # Find nav_get_started line and add after it
    pattern = f'(nav_get_started: "[^"]*",)'
    replacement = f'\\1\n        nav_charting: "{trans["nav_charting"]}",\n        nav_pricing: "{trans["nav_pricing"]}",'
    
    # Only replace once per language block (use counter)
    import re
    matches = list(re.finditer(pattern, content))
    
    # Process from end to start to preserve indices
    lang_order = ['en', 'de', 'tr', 'pt', 'es', 'ru', 'zh', 'ar']
    lang_index = lang_order.index(lang)
    
    if lang_index < len(matches):
        match = matches[lang_index]
        content = content[:match.end()] + f'\n        nav_charting: "{trans["nav_charting"]}",\n        nav_pricing: "{trans["nav_pricing"]}",' + content[match.end():]

with open('translations.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Added nav_charting and nav_pricing to all 8 languages")
