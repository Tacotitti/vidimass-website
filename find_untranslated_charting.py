#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find ALL hardcoded text in Social Media Charting page (without data-i18n)
"""

import sys
import re
from bs4 import BeautifulSoup, NavigableString

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

HTML_FILE = "social-media-charting.html"

def find_untranslated_text():
    """Find all visible text without data-i18n attributes"""
    print("Scanning for hardcoded text without data-i18n...")
    print("=" * 80)
    
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Remove script and style tags
    for script in soup(["script", "style"]):
        script.decompose()
    
    untranslated = []
    
    # Check all text-containing elements
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'li', 'a', 'button', 'th', 'td', 'div', 'label', 'strong', 'em']):
        # Skip if it has data-i18n or data-i18n-html
        if tag.get('data-i18n') or tag.get('data-i18n-html'):
            continue
        
        # Check if parent has data-i18n
        parent_has_i18n = False
        for parent in tag.parents:
            if parent.get('data-i18n') or parent.get('data-i18n-html'):
                parent_has_i18n = True
                break
        
        if parent_has_i18n:
            continue
        
        # Get direct text content (not from children)
        text = ''.join([str(s) for s in tag.contents if isinstance(s, NavigableString)]).strip()
        
        if not text:
            continue
        
        # Skip very short text, numbers, symbols
        if len(text) < 3 or text.isdigit() or re.match(r'^[^\w\s]+$', text):
            continue
        
        # Skip English-only text (likely already correct)
        if re.match(r'^[a-zA-Z0-9\s\-_&]+$', text):
            # But flag if it's clearly a heading or important text
            if tag.name in ['h1', 'h2', 'h3', 'h4', 'p'] and len(text) > 10:
                pass  # Keep for review
            else:
                continue
        
        # This text might need translation
        context = str(tag)[:150]
        untranslated.append({
            'tag': tag.name,
            'text': text,
            'context': context
        })
    
    # Report findings
    print(f"\nFound {len(untranslated)} potential untranslated elements:\n")
    
    for i, item in enumerate(untranslated, 1):
        print(f"{i}. <{item['tag']}> '{item['text'][:80]}'")
        print(f"   Context: {item['context']}")
        print()
    
    if len(untranslated) == 0:
        print("No untranslated text found! Page appears fully translated.")
    
    print("=" * 80)
    print(f"Total: {len(untranslated)} items")

if __name__ == '__main__':
    find_untranslated_text()
