#!/usr/bin/env python3
"""
FINAL CLEANUP - Remove ALL data-i18n attributes from HTML files
"""
import re
import glob

def aggressive_clean_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Change lang to English
    content = re.sub(r'<html lang="[^"]*">', '<html lang="en">', content)
    
    # Remove ALL data-i18n variants (aggressive regex)
    content = re.sub(r'\s*data-i18n(?:-[a-z]+)?="[^"]*"', '', content)
    
    # Remove Language Selector blocks (more aggressive)
    content = re.sub(
        r'<!--\s*Language Selector\s*-->.*?(?=<a\s+href="contact\.html"|</div>\s*<button)',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove script tags for translations
    for script in ['language-preload', 'language', 'language-v2', 'language-v3', 'translations']:
        content = re.sub(rf'\s*<script\s+src="{script}\.js"></script>', '', content)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"OK: {filepath}")

if __name__ == "__main__":
    # Clean all HTML files
    for html_file in glob.glob("*.html"):
        try:
            aggressive_clean_html(html_file)
        except Exception as e:
            print(f"ERROR {html_file}: {e}")
