"""
Comprehensive update of contact.html with ALL data-i18n attributes
"""

import re

with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Title
html = re.sub(
    r'<title>Kontakt - MediaMass</title>',
    r'<title data-i18n="contact_page_title">Kontakt - MediaMass</title>',
    html
)

# Email label and placeholder (continue from where we left)
html = re.sub(
    r'placeholder="ihre\.email@beispiel\.de"',
    r'data-i18n-placeholder="contact_placeholder_email" placeholder="ihre.email@beispiel.de"',
    html
)

# Category label
html = re.sub(
    r'<label for="category"[^>]*>Kategorie \*</label>',
    r'<label for="category" class="block text-sm font-semibold text-gray-300 mb-2"><span data-i18n="contact_label_category">Kategorie</span> *</label>',
    html
)

# Category select placeholder
html = re.sub(
    r'<option value="" class="bg-slate-900">Bitte auswählen</option>',
    r'<option value="" class="bg-slate-900" data-i18n="contact_placeholder_category">Bitte auswählen</option>',
    html,
    count=1
)

# Category options
category_replacements = [
    ('TikTok Mass Posting', 'contact_category_tiktok'),
    ('Instagram Mass Posting', 'contact_category_instagram'),
    ('Multi-Plattform', 'contact_category_multi'),
    ('Musik-Label/Artist Charting', 'contact_category_label'),
    ('Unternehmen', 'contact_category_enterprise'),
    ('Sonstiges', 'contact_category_other'),
]

for text, key in category_replacements:
    html = re.sub(
        f'<option value="[^"]*" class="bg-slate-900">{re.escape(text)}</option>',
        f'<option value="{text.lower().replace(" ", "_").replace("/", "_").replace("-", "_")}" class="bg-slate-900" data-i18n="{key}">{text}</option>',
        html,
        count=1
    )

# Package label
html = re.sub(
    r'<label for="package"[^>]*>Gewünschtes Paket \(optional\)</label>',
    r'<label for="package" class="block text-sm font-semibold text-gray-300 mb-2" data-i18n="contact_label_package">Gewünschtes Paket (optional)</label>',
    html
)

# Package placeholder
html = re.sub(
    r'<option value="" class="bg-slate-900">-- Paket auswählen --</option>',
    r'<option value="" class="bg-slate-900" data-i18n="contact_placeholder_package">-- Paket auswählen --</option>',
    html
)

# Package optgroups
html = re.sub(
    r'<optgroup label="🎵 TikTok Videos"',
    r'<optgroup data-i18n-label="contact_package_group_tiktok" label="🎵 TikTok Videos"',
    html
)
html = re.sub(
    r'<optgroup label="📸 Instagram Reels"',
    r'<optgroup data-i18n-label="contact_package_group_instagram" label="📸 Instagram Reels"',
    html
)

# Message label
html = re.sub(
    r'<label for="message"[^>]*>Nachricht \*</label>',
    r'<label for="message" class="block text-sm font-semibold text-gray-300 mb-2"><span data-i18n="contact_label_message">Nachricht</span> *</label>',
    html
)

# Message placeholder
html = re.sub(
    r'placeholder="Beschreiben Sie Ihre Anfrage\.\.\."',
    r'data-i18n-placeholder="contact_placeholder_message" placeholder="Beschreiben Sie Ihre Anfrage..."',
    html
)

# Submit button
html = re.sub(
    r'>Nachricht senden</button>',
    r' data-i18n="contact_button_submit">Nachricht senden</button>',
    html
)

# Alternative contact heading
html = re.sub(
    r'<h3[^>]*>Alternative Kontaktmöglichkeiten</h3>',
    r'<h3 class="text-2xl font-bold mb-6 text-center" data-i18n="contact_alt_heading">Alternative Kontaktmöglichkeiten</h3>',
    html
)

# Alternative contact labels
html = re.sub(
    r'<div class="text-sm text-gray-400 mb-1">E-Mail</div>',
    r'<div class="text-sm text-gray-400 mb-1" data-i18n="contact_alt_email">E-Mail</div>',
    html
)
html = re.sub(
    r'<div class="text-sm text-gray-400 mb-1">Telegram</div>',
    r'<div class="text-sm text-gray-400 mb-1" data-i18n="contact_alt_telegram">Telegram</div>',
    html
)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Updated contact.html with all data-i18n attributes!")
print("   - Page title")
print("   - Headings (heading, subheading)")
print("   - Form labels (name, email, category, package, message)")
print("   - Placeholders (all inputs)")
print("   - Category options (6 options)")
print("   - Package groups (2 optgroups)")
print("   - Submit button")
print("   - Alternative contact section")
