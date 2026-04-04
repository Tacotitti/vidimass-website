"""
Batch update: Add data-i18n to common elements across ALL pages
- Footer terms/copyright
- CTA buttons
- Common navigation elements
"""

import re
import os

pages = ['index.html', 'preisliste.html', 'contact.html', 
         'social-media-charting.html', 'datenschutz.html', 'nutzungsbedingungen.html']

replacements = [
    # Footer - Terms link
    (
        r'<a href="nutzungsbedingungen\.html"([^>]*)>Nutzungsbedingungen</a>',
        r'<a href="nutzungsbedingungen.html"\1><span data-i18n="footer_terms">Nutzungsbedingungen</span></a>'
    ),
    # Footer - Copyright (handle special character)
    (
        r'<div class="text-gray-500 text-sm">\s*[©Â©]\s*2026 MediaMass\.[^<]*</div>',
        r'<div class="text-gray-500 text-sm" data-i18n="footer_copyright">© 2026 MediaMass. Alle Rechte vorbehalten.</div>'
    ),
    # CTA Button "Jetzt starten" / "Get Started"
    (
        r'>Jetzt starten</a>',
        r' data-i18n="cta_get_started">Jetzt starten</a>'
    ),
    # Contact button
    (
        r'>Kontakt</a>',
        r' data-i18n="cta_contact">Kontakt</a>'
    ),
]

for page in pages:
    if not os.path.exists(page):
        continue
    
    print(f"\n📄 Processing {page}...")
    
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes = 0
    for pattern, replacement in replacements:
        matches = len(re.findall(pattern, content))
        if matches > 0:
            content = re.sub(pattern, replacement, content)
            changes += matches
            print(f"   ✓ Applied pattern (found {matches} matches)")
    
    if changes > 0:
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   ✅ Saved {changes} changes")
    else:
        print(f"   ⚠️  No changes")

print("\n✅ Batch update complete!")
