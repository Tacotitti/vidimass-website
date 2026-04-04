"""
Comprehensive audit: Find all text content that needs data-i18n attributes
"""

import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Find all text elements without data-i18n
elements_to_translate = []

# Hero section
hero = soup.find('section', class_='hero-section')
if hero:
    print("=== HERO SECTION ===")
    # Title lines
    h1 = hero.find('h1')
    if h1:
        for span in h1.find_all('span'):
            text = span.get_text(strip=True)
            has_i18n = span.get('data-i18n')
            if text and not has_i18n:
                print(f"❌ H1: '{text}' - NO data-i18n")
    
    # Subtitle
    h2 = hero.find('h2')
    if h2:
        text = h2.get_text(strip=True)[:100]
        has_i18n = h2.get('data-i18n')
        if not has_i18n:
            print(f"❌ H2 Subtitle: '{text}...' - NO data-i18n")

# Features section subtitle
features = soup.find('section', id='features')
if features:
    print("\n=== FEATURES SECTION ===")
    subtitle = features.find('p', class_='text-xl')
    if subtitle:
        text = subtitle.get_text(strip=True)
        has_i18n = subtitle.get('data-i18n') or subtitle.find('span', {'data-i18n': True})
        if not has_i18n:
            print(f"❌ Subtitle: '{text}' - NO data-i18n")

print("\n=== RECOMMENDATION ===")
print("Add data-i18n to:")
print("1. Hero H1 title (3 lines)")
print("2. Hero H2 subtitle (full text)")
print("3. Features subtitle")
print("4. ALL other visible text")
