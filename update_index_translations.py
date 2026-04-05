"""
Update index.html - add data-i18n to ALL visible German text
Priority: Most visible elements first
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# List of replacements (pattern, replacement)
replacements = [
    # Section title
    (
        r'<span class="bg-gradient-to-r from-violet-400 to-pink-400 bg-clip-text text-transparent">Charting für Labels</span>',
        r'<span class="bg-gradient-to-r from-violet-400 to-pink-400 bg-clip-text text-transparent" data-i18n="home_section_title_1">Charting für Labels</span>'
    ),
    (
        r'<span class="text-white">und Künstler weltweit</span>',
        r'<span class="text-white" data-i18n="home_section_title_2">und Künstler weltweit</span>'
    ),
    
    # SEO Section Title
    (
        r'<h2 class="text-3xl md:text-4xl font-bold mb-6 bg-gradient-to-r from-violet-400 to-pink-400 bg-clip-text text-transparent">Mass Posting für TikTok, Instagram & Spotify Charting</h2>',
        r'<h2 class="text-3xl md:text-4xl font-bold mb-6 bg-gradient-to-r from-violet-400 to-pink-400 bg-clip-text text-transparent" data-i18n="seo_title">Mass Posting für TikTok, Instagram & Spotify Charting</h2>'
    ),
    
    # SEO Paragraphs
    (
        r'<p class="text-lg text-gray-300 mb-4">\s*<strong>MediaMass</strong>\s*ist der\s*<strong class="text-violet-400">führende</strong>\s*<strong class="text-pink-400">Mass Posting Service</strong>.*?</p>',
        r'<p class="text-lg text-gray-300 mb-4" data-i18n-html="seo_intro_p1"><strong>MediaMass</strong> ist der <strong class="text-violet-400">führende</strong> <strong class="text-pink-400">Mass Posting Service</strong> für die Musikindustrie. Unser professionelles Mass Posting System ermöglicht es Künstlern, Labels und Marken, bis zu 250.000 Videos täglich auf TikTok, Instagram und weiteren Plattformen zu verbreiten.</p>'
    ),
    (
        r'<p class="text-gray-300 mb-4">Unser\s*<strong class="text-cyan-400">Mass Posting Service</strong>.*?</p>',
        r'<p class="text-gray-300 mb-4" data-i18n-html="seo_intro_p2">Unser <strong class="text-cyan-400">Mass Posting Service</strong> nutzt fortschrittliche Algorithmen für TikTok Mass Posting und Instagram Mass Post. Erreichen Sie maximale Reichweite durch Social Media Charting und virales Marketing.</p>'
    ),
    
    # Service Cards
    (
        r'<h4 class="text-xl font-bold text-white mb-3">🎵 TikTok Mass Posting</h4>',
        r'<h4 class="text-xl font-bold text-white mb-3" data-i18n="service_tiktok_title">🎵 TikTok Mass Posting</h4>'
    ),
    (
        r'<p class="text-gray-300 text-sm mb-3">\s*<strong>Professionelles</strong>\s*<strong class="text-cyan-400">TikTok Mass Posting</strong>.*?</p>',
        r'<p class="text-gray-300 text-sm mb-3" data-i18n-html="service_tiktok_desc"><strong>Professionelles</strong> <strong class="text-cyan-400">TikTok Mass Posting</strong> mit bis zu 100.000 Videos pro Tag. Erreichen Sie die TikTok Trending Page und pushen Sie Ihre Songs in die Spotify Viral Charts.</p>'
    ),
    (
        r'<h4 class="text-xl font-bold text-white mb-3">📸 Instagram Mass Post</h4>',
        r'<h4 class="text-xl font-bold text-white mb-3" data-i18n="service_instagram_title">📸 Instagram Mass Post</h4>'
    ),
    (
        r'<p class="text-gray-300 text-sm mb-3">\s*<strong>Automatischer</strong>\s*<strong class="text-pink-400">Instagram Mass Post</strong>.*?</p>',
        r'<p class="text-gray-300 text-sm mb-3" data-i18n-html="service_instagram_desc"><strong>Automatischer</strong> <strong class="text-pink-400">Instagram Mass Post</strong> für Reels, Stories und Feed. Maximale Reichweite durch virales Mass Posting.</p>'
    ),
    (
        r'<h4 class="text-xl font-bold text-white mb-3">🎧 Spotify Charting</h4>',
        r'<h4 class="text-xl font-bold text-white mb-3" data-i18n="service_spotify_title">🎧 Spotify Charting</h4>'
    ),
    (
        r'<p class="text-gray-300 text-sm mb-3">\s*<strong>Durch</strong>\s*<strong class="text-cyan-400">TikTok Mass Posting</strong>.*?</p>',
        r'<p class="text-gray-300 text-sm mb-3" data-i18n-html="service_spotify_desc"><strong>Durch</strong> <strong class="text-cyan-400">TikTok Mass Posting</strong> erreichen Sie automatisch Spotify Viral Charts, Apple Music und weitere Streaming-Plattformen. Mass Post = Chart-Erfolg.</p>'
    ),
    
    # Why Section
    (
        r'<h3 class="text-2xl font-bold text-white mb-6">Warum Mass Posting mit MediaMass\?</h3>',
        r'<h3 class="text-2xl font-bold text-white mb-6" data-i18n="why_title">Warum Mass Posting mit MediaMass?</h3>'
    ),
    (
        r'<h4 class="font-semibold text-violet-400 mb-2">🚀 Schnellste Mass Post Lösung</h4>',
        r'<h4 class="font-semibold text-violet-400 mb-2" data-i18n="why_1_title">🚀 Schnellste Mass Post Lösung</h4>'
    ),
    (
        r'<p class="text-gray-300 text-sm">\s*<strong>Unser</strong>\s*<strong class="text-violet-400">Mass Posting System</strong>\s*ist 10x schneller.*?</p>',
        r'<p class="text-gray-300 text-sm" data-i18n-html="why_1_desc"><strong>Unser</strong> <strong class="text-violet-400">Mass Posting System</strong> ist 10x schneller als manuelle Methoden. 250.000 Videos in 24 Stunden.</p>'
    ),
    (
        r'<h4 class="font-semibold text-pink-400 mb-2">📊 Social Media Charting Garantie</h4>',
        r'<h4 class="font-semibold text-pink-400 mb-2" data-i18n="why_2_title">📊 Social Media Charting Garantie</h4>'
    ),
    (
        r'<p class="text-gray-300 text-sm">\s*<strong>Mit</strong>\s*<strong class="text-cyan-400">TikTok Mass Posting</strong>\s*erreichen Sie garantiert.*?</p>',
        r'<p class="text-gray-300 text-sm" data-i18n-html="why_2_desc"><strong>Mit</strong> <strong class="text-cyan-400">TikTok Mass Posting</strong> erreichen Sie garantiert die TikTok Trending Page und SoundOn Charts.</p>'
    ),
    (
        r'<h4 class="font-semibold text-green-400 mb-2">💰 Beste Mass Posting Preise</h4>',
        r'<h4 class="font-semibold text-green-400 mb-2" data-i18n="why_3_title">💰 Beste Mass Posting Preise</h4>'
    ),
    (
        r'<p class="text-gray-300 text-sm">Ab \$0\.079 pro TikTok Video.*?</p>',
        r'<p class="text-gray-300 text-sm" data-i18n="why_3_desc">Ab $0.079 pro TikTok Video. Keine versteckten Gebühren. Transparente Mass Post Preise.</p>'
    ),
    (
        r'<h4 class="font-semibold text-orange-400 mb-2">🎯 Automatisierter Instagram Mass Post</h4>',
        r'<h4 class="font-semibold text-orange-400 mb-2" data-i18n="why_4_title">🎯 Automatisierter Instagram Mass Post</h4>'
    ),
    (
        r'<p class="text-gray-300 text-sm">Vollautomatisches Instagram Mass Posting.*?</p>',
        r'<p class="text-gray-300 text-sm" data-i18n="why_4_desc">Vollautomatisches Instagram Mass Posting für Reels. Mehr Reichweite, mehr Engagement, mehr Erfolg.</p>'
    ),
]

changes = 0
for pattern, replacement in replacements:
    if re.search(pattern, html, re.DOTALL):
        html = re.sub(pattern, replacement, html, flags=re.DOTALL)
        changes += 1
        print(f"✓ Applied replacement {changes}")
    else:
        print(f"⚠️  Pattern not found: {pattern[:50]}...")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✅ Updated index.html with {changes} changes")
