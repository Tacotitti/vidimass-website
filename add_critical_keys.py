"""
Add critical translation keys for Homepage content
Focus on visible text that appears when switching to English
"""

import json

# Keys to add (after existing keys)
new_keys_en = {
    # Page Titles
    'page_title_home': 'Mass Posting Service for TikTok, Instagram & Spotify Charting | MediaMass - Up to 250,000 Videos Daily',
    'page_title_pricing': 'Pricing - Video Distribution Packages | MediaMass',
    
    # Homepage Section
    'home_section_title_1': 'Charting for Labels',
    'home_section_title_2': 'and Artists Worldwide',
    
    # Features
    'feature_2_desc': 'TikTok users who hear your song in creations stream it 23x more on Spotify. High-volume posting = chart success',
    
    # SEO Section
    'seo_title': 'Mass Posting for TikTok, Instagram & Spotify Charting',
    'seo_intro_p1': 'MediaMass is the leading Mass Posting Service for the music industry. Our professional Mass Posting System enables artists, labels, and brands to distribute up to 250,000 videos daily across TikTok, Instagram, and other platforms.',
    'seo_intro_p2': 'Our Mass Posting Service uses advanced algorithms for TikTok Mass Posting and Instagram Mass Post. Achieve maximum reach through Social Media Charting and viral marketing.',
    
    # Service Cards
    'service_tiktok_title': '🎵 TikTok Mass Posting',
    'service_tiktok_desc': 'Professional TikTok Mass Posting with up to 100,000 videos per day. Reach the TikTok Trending Page and boost your songs onto Spotify Viral Charts.',
    'service_tiktok_link': 'Learn More About TikTok Charting',
    
    'service_instagram_title': '📸 Instagram Mass Post',
    'service_instagram_desc': 'Automated Instagram Mass Post for Reels, Stories, and Feed. Maximum reach through viral mass posting.',
    'service_instagram_link': 'Instagram Posting Packages',
    
    'service_spotify_title': '🎧 Spotify Charting',
    'service_spotify_desc': 'Through TikTok Mass Posting, automatically reach Spotify Viral Charts, Apple Music, and other streaming platforms. Mass Post = Chart Success.',
    'service_spotify_link': 'Get Started Now',
    
    # Why Section
    'why_title': 'Why Mass Posting with MediaMass?',
    'why_1_title': '🚀 Fastest Mass Post Solution',
    'why_1_desc': 'Our Mass Posting System is 10x faster than manual methods. 250,000 videos in 24 hours.',
    'why_2_title': '📊 Social Media Charting Guarantee',
    'why_2_desc': 'With TikTok Mass Posting, you are guaranteed to reach the TikTok Trending Page and SoundOn Charts.',
    'why_3_title': '💰 Best Mass Posting Prices',
    'why_3_desc': 'Starting from $0.079 per TikTok video. No hidden fees. Transparent Mass Post pricing.',
    'why_4_title': '🎯 Automated Instagram Mass Post',
    'why_4_desc': 'Fully automated Instagram Mass Posting for Reels. More reach, more engagement, more success.',
    
    # Pricing Page
    'pricing_hero_title': 'Video Distribution Packages',
    'pricing_hero_desc': 'Transparent Prices for TikTok and Instagram Mass Posting',
    'pricing_tiktok_title': '🎵 TikTok Video Distribution',
    'pricing_tiktok_desc': 'Mass Video Posting for TikTok',
    'pricing_instagram_title': '📸 Instagram Reels Distribution',
    'pricing_instagram_desc': 'Unique Reels for Instagram Mass Posting',
    'pricing_table_videos': 'Videos',
    'pricing_table_price': 'Price',
    'pricing_table_per_video': 'Per Video',
    'pricing_table_reels': 'Unique Reels',
    'pricing_custom_note': '💡 Custom Volumes: Any quantity over 125K Reels at a flat rate of €0.026 per Reel',
    'pricing_cta_title': 'Custom Packages Available',
    'pricing_cta_desc': 'Need a custom package or have questions about our pricing?',
}

new_keys_de = {
    'page_title_home': 'Mass Posting Service für TikTok, Instagram & Spotify Charting | MediaMass - Bis zu 250.000 Videos täglich',
    'page_title_pricing': 'Preisliste - Video Distribution Pakete | MediaMass',
    
    'home_section_title_1': 'Charting für Labels',
    'home_section_title_2': 'und Künstler weltweit',
    
    'feature_2_desc': 'TikTok users who hear your song in creations stream it 23x more on Spotify. High-volume posting = Chart-Erfolg',
    
    'seo_title': 'Mass Posting für TikTok, Instagram & Spotify Charting',
    'seo_intro_p1': 'MediaMass ist der führende Mass Posting Service für die Musikindustrie. Unser professionelles Mass Posting System ermöglicht es Künstlern, Labels und Marken, bis zu 250.000 Videos täglich auf TikTok, Instagram und weiteren Plattformen zu verbreiten.',
    'seo_intro_p2': 'Unser Mass Posting Service nutzt fortschrittliche Algorithmen für TikTok Mass Posting und Instagram Mass Post. Erreichen Sie maximale Reichweite durch Social Media Charting und virales Marketing.',
    
    'service_tiktok_title': '🎵 TikTok Mass Posting',
    'service_tiktok_desc': 'Professionelles TikTok Mass Posting mit bis zu 100.000 Videos pro Tag. Erreichen Sie die TikTok Trending Page und pushen Sie Ihre Songs in die Spotify Viral Charts.',
    'service_tiktok_link': 'Mehr über TikTok Charting',
    
    'service_instagram_title': '📸 Instagram Mass Post',
    'service_instagram_desc': 'Automatischer Instagram Mass Post für Reels, Stories und Feed. Maximale Reichweite durch virales Mass Posting.',
    'service_instagram_link': 'Instagram Posting Pakete',
    
    'service_spotify_title': '🎧 Spotify Charting',
    'service_spotify_desc': 'Durch TikTok Mass Posting erreichen Sie automatisch Spotify Viral Charts, Apple Music und weitere Streaming-Plattformen. Mass Post = Chart-Erfolg.',
    'service_spotify_link': 'Jetzt starten',
    
    'why_title': 'Warum Mass Posting mit MediaMass?',
    'why_1_title': '🚀 Schnellste Mass Post Lösung',
    'why_1_desc': 'Unser Mass Posting System ist 10x schneller als manuelle Methoden. 250.000 Videos in 24 Stunden.',
    'why_2_title': '📊 Social Media Charting Garantie',
    'why_2_desc': 'Mit TikTok Mass Posting erreichen Sie garantiert die TikTok Trending Page und SoundOn Charts.',
    'why_3_title': '💰 Beste Mass Posting Preise',
    'why_3_desc': 'Ab $0.079 pro TikTok Video. Keine versteckten Gebühren. Transparente Mass Post Preise.',
    'why_4_title': '🎯 Automatisierter Instagram Mass Post',
    'why_4_desc': 'Vollautomatisches Instagram Mass Posting für Reels. Mehr Reichweite, mehr Engagement, mehr Erfolg.',
    
    'pricing_hero_title': 'Video Distribution Pakete',
    'pricing_hero_desc': 'Transparente Preise für TikTok und Instagram Mass Posting',
    'pricing_tiktok_title': '🎵 TikTok Video Distribution',
    'pricing_tiktok_desc': 'Mass Video Posting für TikTok',
    'pricing_instagram_title': '📸 Instagram Reels Distribution',
    'pricing_instagram_desc': 'Unique Reels für Instagram Mass Posting',
    'pricing_table_videos': 'Videos',
    'pricing_table_price': 'Preis',
    'pricing_table_per_video': 'Pro Video',
    'pricing_table_reels': 'Unique Reels',
    'pricing_custom_note': '💡 Custom Volumes: Beliebige Menge über 125K Reels zum Flat-Rate-Preis von €0.026 pro Reel',
    'pricing_cta_title': 'Individuelle Pakete verfügbar',
    'pricing_cta_desc': 'Benötigen Sie ein Custom Package oder haben Fragen zu unseren Preisen?',
}

# Read translations.js
with open('translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last key in EN section and add new keys
import re

# Find the EN section
en_match = re.search(r'(en:\s*\{[^}]+)(contact_alt_telegram:\s*"[^"]*",)', content, re.DOTALL)
if en_match:
    insert_pos = en_match.end()
    
    # Build insertion string
    en_insertion = '\n'
    for key, value in new_keys_en.items():
        value_escaped = value.replace('"', '\\"')
        en_insertion += f'        {key}: "{value_escaped}",\n'
    
    content = content[:insert_pos] + en_insertion + content[insert_pos:]
    print(f"✓ Added {len(new_keys_en)} keys to EN")
else:
    print("❌ Could not find EN insertion point")

# Same for DE
de_match = re.search(r'(de:\s*\{[^}]+)(contact_alt_telegram:\s*"[^"]*",)', content, re.DOTALL)
if de_match:
    insert_pos = de_match.end()
    
    de_insertion = '\n'
    for key, value in new_keys_de.items():
        value_escaped = value.replace('"', '\\"')
        de_insertion += f'        {key}: "{value_escaped}",\n'
    
    content = content[:insert_pos] + de_insertion + content[insert_pos:]
    print(f"✓ Added {len(new_keys_de)} keys to DE")
else:
    print("❌ Could not find DE insertion point")

# Write back
with open('translations.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ Critical translation keys added!")
print(f"Total new keys per language: {len(new_keys_en)}")
