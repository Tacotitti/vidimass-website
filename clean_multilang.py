#!/usr/bin/env python3
"""
Remove multilingual system from HTML files - English only
"""
import re
import sys

def clean_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Change lang to English
    content = re.sub(r'<html lang="[^"]*">', '<html lang="en">', content)
    
    # 2. Remove Desktop Language Selector (aggressive)
    content = re.sub(
        r'<!--\s*Language Selector\s*-->.*?</div>\s*</div>\s*\n\s*<a href="contact\.html"',
        '<a href="contact.html"',
        content,
        flags=re.DOTALL
    )
    
    # 3. Remove Mobile Language Selector (if exists)
    content = re.sub(
        r'<!--\s*Mobile Language Menu\s*-->.*?</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # 4. Remove all data-i18n attributes
    content = re.sub(r'\s*data-i18n="[^"]*"', '', content)
    content = re.sub(r'\s*data-i18n-html="[^"]*"', '', content)
    content = re.sub(r'\s*data-i18n-placeholder="[^"]*"', '', content)
    content = re.sub(r'\s*data-i18n-label="[^"]*"', '', content)
    
    # 5. Remove translation script tags
    content = re.sub(r'\s*<script src="language-preload\.js"></script>', '', content)
    content = re.sub(r'\s*<script src="language\.js"></script>', '', content)
    content = re.sub(r'\s*<script src="language-v2\.js"></script>', '', content)
    content = re.sub(r'\s*<script src="language-v3\.js"></script>', '', content)
    content = re.sub(r'\s*<script src="translations\.js"></script>', '', content)
    
    # Write cleaned version
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"OK Cleaned: {filepath}")

if __name__ == "__main__":
    files = [
        "social-media-charting.html",
        "datenschutz.html",
        "nutzungsbedingungen.html"
    ]
    
    for file in files:
        try:
            clean_html(file)
        except Exception as e:
            print(f"ERROR cleaning {file}: {e}")
