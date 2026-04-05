"""
Remove Russian, Chinese, Arabic languages from language selector
Keep only: EN, DE, TR, PT, ES (5 languages)
"""

import re

pages = ['index.html', 'preisliste.html', 'contact.html', 'social-media-charting.html', 
         'datenschutz.html', 'nutzungsbedingungen.html']

# Languages to remove
remove_langs = ['ru', 'zh', 'ar']

for page in pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Remove RU button
        html = re.sub(
            r'<button class="lang-option" data-lang="ru">.*?</button>\s*',
            '',
            html,
            flags=re.DOTALL
        )
        
        # Remove ZH button
        html = re.sub(
            r'<button class="lang-option" data-lang="zh">.*?</button>\s*',
            '',
            html,
            flags=re.DOTALL
        )
        
        # Remove AR button
        html = re.sub(
            r'<button class="lang-option" data-lang="ar">.*?</button>\s*',
            '',
            html,
            flags=re.DOTALL
        )
        
        with open(page, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✓ Removed RU, ZH, AR from {page}")
    
    except FileNotFoundError:
        print(f"⚠ File not found: {page}")

print("\n✅ Language selector updated on all pages!")
print("Remaining languages: EN, DE, TR, PT, ES")
