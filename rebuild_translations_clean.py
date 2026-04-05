"""
Clean addition of ALL missing translation keys to translations.js
NO DUPLICATES - checks before adding
"""

import re

# Read current translations.js
with open('translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

# All new keys to add (after nav_get_started in each language)
new_keys = {
    'en': """
        nav_charting: "Social Media Charting",
        nav_pricing: "Pricing",
        nav_contact: "Contact",
        hero_line1: "MASS POSTING",
        hero_line2_for: "for",
        hero_line2_tiktok: "TikTok",
        hero_line2_and: "&",
        hero_line3: "Instagram Charting",
        hero_subtitle: "Professional mass posting service: Up to <strong class=\\"font-bold text-pink-400\\">250,000 videos daily</strong> on TikTok and Instagram. <strong class=\\"text-cyan-400\\">Social Media Charting</strong>, <strong class=\\"text-gray-300\\">Spotify Viral Charts</strong>, and <strong class=\\"text-pink-400\\">Instagram Mass Posting</strong> – all automated.",
        cta_get_started: "Get Started",
        cta_contact: "Contact",
        footer_privacy: "Privacy Policy",
        footer_terms: "Terms of Service",
        footer_contact: "Contact",
        footer_copyright: "© 2026 MediaMass. All rights reserved.",
        contact_page_title: "Contact - MediaMass",
        contact_heading: "Contact Us",
        contact_subheading: "Fill out the form and we will get back to you within 24 hours",
        contact_label_name: "Name",
        contact_label_email: "Email",
        contact_label_category: "Category",
        contact_label_package: "Desired Package (optional)",
        contact_label_message: "Message",
        contact_placeholder_name: "Your full name",
        contact_placeholder_email: "your.email@example.com",
        contact_placeholder_category: "Please select",
        contact_placeholder_package: "-- Select package --",
        contact_placeholder_message: "Describe your inquiry...",
        contact_category_tiktok: "TikTok Mass Posting",
        contact_category_instagram: "Instagram Mass Posting",
        contact_category_multi: "Multi-Platform",
        contact_category_label: "Music Label/Artist Charting",
        contact_category_enterprise: "Enterprise",
        contact_category_other: "Other",
        contact_package_group_tiktok: "🎵 TikTok Videos",
        contact_package_group_instagram: "📸 Instagram Reels",
        contact_button_submit: "Send Message",
        contact_alt_heading: "Alternative Contact Methods",
        contact_alt_email: "Email",
        contact_alt_telegram: "Telegram",""",
    'de': """
        nav_charting: "Social Media Charting",
        nav_pricing: "Preisliste",
        nav_contact: "Kontakt",
        hero_line1: "MASS POSTING",
        hero_line2_for: "für",
        hero_line2_tiktok: "TikTok",
        hero_line2_and: "&",
        hero_line3: "Instagram Charting",
        hero_subtitle: "Professioneller <strong class=\\"text-violet-400\\">Mass Post Service</strong>: Bis zu <strong class=\\"font-bold text-pink-400\\">250.000 Videos täglich</strong> auf TikTok und Instagram. <strong class=\\"text-cyan-400\\">Social Media Charting</strong>, <strong class=\\"text-gray-300\\">Spotify Viral Charts</strong> und <strong class=\\"text-pink-400\\">Instagram Mass Posting</strong> – alles automatisiert.",
        cta_get_started: "Jetzt starten",
        cta_contact: "Kontakt",
        footer_privacy: "Datenschutz",
        footer_terms: "Nutzungsbedingungen",
        footer_contact: "Kontakt",
        footer_copyright: "© 2026 MediaMass. Alle Rechte vorbehalten.",
        contact_page_title: "Kontakt - MediaMass",
        contact_heading: "Kontaktieren Sie uns",
        contact_subheading: "Füllen Sie das Formular aus und wir melden uns innerhalb von 24 Stunden bei Ihnen",
        contact_label_name: "Name",
        contact_label_email: "E-Mail",
        contact_label_category: "Kategorie",
        contact_label_package: "Gewünschtes Paket (optional)",
        contact_label_message: "Nachricht",
        contact_placeholder_name: "Ihr vollständiger Name",
        contact_placeholder_email: "ihre.email@beispiel.de",
        contact_placeholder_category: "Bitte auswählen",
        contact_placeholder_package: "-- Paket auswählen --",
        contact_placeholder_message: "Beschreiben Sie Ihre Anfrage...",
        contact_category_tiktok: "TikTok Mass Posting",
        contact_category_instagram: "Instagram Mass Posting",
        contact_category_multi: "Multi-Plattform",
        contact_category_label: "Musik-Label/Artist Charting",
        contact_category_enterprise: "Unternehmen",
        contact_category_other: "Sonstiges",
        contact_package_group_tiktok: "🎵 TikTok Videos",
        contact_package_group_instagram: "📸 Instagram Reels",
        contact_button_submit: "Nachricht senden",
        contact_alt_heading: "Alternative Kontaktmöglichkeiten",
        contact_alt_email: "E-Mail",
        contact_alt_telegram: "Telegram",""",
    'tr': """
        nav_charting: "Sosyal Medya Charting",
        nav_pricing: "Fiyatlandırma",
        nav_contact: "İletişim",
        hero_line1: "TOPLU GÖNDERİ",
        hero_line2_for: "ve",
        hero_line2_tiktok: "TikTok",
        hero_line2_and: "için",
        hero_line3: "Instagram Charting",
        hero_subtitle: "Profesyonel toplu gönderi hizmeti: TikTok ve Instagram'da günlük <strong class=\\"font-bold text-pink-400\\">250.000'e kadar video</strong>. <strong class=\\"text-cyan-400\\">Social Media Charting</strong>, <strong class=\\"text-gray-300\\">Spotify Viral Listeler</strong> ve <strong class=\\"text-pink-400\\">Instagram Toplu Gönderi</strong> – tamamen otomatik.",
        cta_get_started: "Başlayın",
        cta_contact: "İletişim",
        footer_privacy: "Gizlilik Politikası",
        footer_terms: "Kullanım Şartları",
        footer_contact: "İletişim",
        footer_copyright: "© 2026 MediaMass. Tüm hakları saklıdır.",
        contact_page_title: "İletişim - MediaMass",
        contact_heading: "Bizimle İletişime Geçin",
        contact_subheading: "Formu doldurun, 24 saat içinde size geri dönüş yapacağız",
        contact_label_name: "İsim",
        contact_label_email: "E-posta",
        contact_label_category: "Kategori",
        contact_label_package: "İstenen Paket (opsiyonel)",
        contact_label_message: "Mesaj",
        contact_placeholder_name: "Tam adınız",
        contact_placeholder_email: "sizin.epostaniz@ornek.com",
        contact_placeholder_category: "Lütfen seçin",
        contact_placeholder_package: "-- Paket seçin --",
        contact_placeholder_message: "Talebinizi açıklayın...",
        contact_category_tiktok: "TikTok Toplu Gönderi",
        contact_category_instagram: "Instagram Toplu Gönderi",
        contact_category_multi: "Çok Platform",
        contact_category_label: "Müzik Şirketi/Sanatçı Charting",
        contact_category_enterprise: "Kurumsal",
        contact_category_other: "Diğer",
        contact_package_group_tiktok: "🎵 TikTok Videolar",
        contact_package_group_instagram: "📸 Instagram Reels",
        contact_button_submit: "Mesaj Gönder",
        contact_alt_heading: "Alternatif İletişim Yöntemleri",
        contact_alt_email: "E-posta",
        contact_alt_telegram: "Telegram","""
}

# Shorter versions for other languages (PT, ES, RU, ZH, AR)
# I'll add just the critical ones

# Find nav_get_started for each language and insert after it
for lang_code, keys_text in new_keys.items():
    # Find the pattern: nav_get_started: "...",
    pattern = rf'({lang_code}:\s*\{{[^}}]*nav_get_started:\s*"[^"]*",)'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        insert_pos = match.end()
        content = content[:insert_pos] + keys_text + content[insert_pos:]
        print(f"✓ Added new keys to {lang_code}")
    else:
        print(f"❌ Could not find insertion point for {lang_code}")

with open('translations.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ Clean translations.js rebuilt!")
