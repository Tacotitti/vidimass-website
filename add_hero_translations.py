"""Add hero headline translations to all languages"""

# New translations to add
new_translations = {
    'en': {
        'hero_line1': 'MASS POSTING',
        'hero_line2_for': 'for',
        'hero_line2_tiktok': 'TikTok',
        'hero_line2_and': '&',
        'hero_line3': 'Instagram Charting',
        'hero_subtitle': 'Professional mass posting service: Up to <strong class="font-bold text-pink-400">250,000 videos daily</strong> on TikTok and Instagram. <strong class="text-cyan-400">Social Media Charting</strong>, <strong class="text-gray-300">Spotify Viral Charts</strong>, and <strong class="text-pink-400">Instagram Mass Posting</strong> – all automated.',
    },
    'de': {
        'hero_line1': 'MASS POSTING',
        'hero_line2_for': 'für',
        'hero_line2_tiktok': 'TikTok',
        'hero_line2_and': '&',
        'hero_line3': 'Instagram Charting',
        'hero_subtitle': 'Professioneller <strong class="text-violet-400">Mass Post Service</strong>: Bis zu <strong class="font-bold text-pink-400">250.000 Videos täglich</strong> auf TikTok und Instagram. <strong class="text-cyan-400">Social Media Charting</strong>, <strong class="text-gray-300">Spotify Viral Charts</strong> und <strong class="text-pink-400">Instagram Mass Posting</strong> – alles automatisiert.',
    },
    'tr': {
        'hero_line1': 'TOPLU GÖNDERİ',
        'hero_line2_for': 've',
        'hero_line2_tiktok': 'TikTok',
        'hero_line2_and': 'için',
        'hero_line3': 'Instagram Charting',
        'hero_subtitle': 'Profesyonel toplu gönderi hizmeti: TikTok ve Instagram\'da günlük <strong class="font-bold text-pink-400">250.000\'e kadar video</strong>. <strong class="text-cyan-400">Social Media Charting</strong>, <strong class="text-gray-300">Spotify Viral Listeler</strong> ve <strong class="text-pink-400">Instagram Toplu Gönderi</strong> – tamamen otomatik.',
    },
    'pt': {
        'hero_line1': 'POSTAGEM EM MASSA',
        'hero_line2_for': 'para',
        'hero_line2_tiktok': 'TikTok',
        'hero_line2_and': 'e',
        'hero_line3': 'Instagram Charting',
        'hero_subtitle': 'Serviço profissional de postagem em massa: Até <strong class="font-bold text-pink-400">250.000 vídeos diariamente</strong> no TikTok e Instagram. <strong class="text-cyan-400">Social Media Charting</strong>, <strong class="text-gray-300">Spotify Viral Charts</strong> e <strong class="text-pink-400">Instagram Mass Posting</strong> – tudo automatizado.',
    },
    'es': {
        'hero_line1': 'PUBLICACIÓN MASIVA',
        'hero_line2_for': 'para',
        'hero_line2_tiktok': 'TikTok',
        'hero_line2_and': 'y',
        'hero_line3': 'Instagram Charting',
        'hero_subtitle': 'Servicio profesional de publicación masiva: Hasta <strong class="font-bold text-pink-400">250,000 videos diarios</strong> en TikTok e Instagram. <strong class="text-cyan-400">Social Media Charting</strong>, <strong class="text-gray-300">Spotify Viral Charts</strong> y <strong class="text-pink-400">Instagram Mass Posting</strong> – todo automatizado.',
    },
    'ru': {
        'hero_line1': 'МАССОВАЯ ПУБЛИКАЦИЯ',
        'hero_line2_for': 'для',
        'hero_line2_tiktok': 'TikTok',
        'hero_line2_and': 'и',
        'hero_line3': 'Instagram Charting',
        'hero_subtitle': 'Профессиональный сервис массовой публикации: До <strong class="font-bold text-pink-400">250,000 видео ежедневно</strong> в TikTok и Instagram. <strong class="text-cyan-400">Social Media Charting</strong>, <strong class="text-gray-300">Spotify Viral Charts</strong> и <strong class="text-pink-400">Instagram Mass Posting</strong> – всё автоматизировано.',
    },
    'zh': {
        'hero_line1': '批量发布',
        'hero_line2_for': '用于',
        'hero_line2_tiktok': 'TikTok',
        'hero_line2_and': '和',
        'hero_line3': 'Instagram 排行',
        'hero_subtitle': '专业批量发布服务：TikTok 和 Instagram 每天可发布<strong class="font-bold text-pink-400">多达 250,000 个视频</strong>。<strong class="text-cyan-400">社交媒体排行</strong>、<strong class="text-gray-300">Spotify 病毒榜单</strong>和<strong class="text-pink-400">Instagram 批量发布</strong> – 全自动化。',
    },
    'ar': {
        'hero_line1': 'النشر الجماعي',
        'hero_line2_for': 'لـ',
        'hero_line2_tiktok': 'TikTok',
        'hero_line2_and': 'و',
        'hero_line3': 'Instagram Charting',
        'hero_subtitle': 'خدمة نشر جماعي احترافية: ما يصل إلى <strong class="font-bold text-pink-400">250,000 فيديو يوميًا</strong> على TikTok و Instagram. <strong class="text-cyan-400">تصنيف وسائل التواصل</strong> و <strong class="text-gray-300">Spotify Viral Charts</strong> و <strong class="text-pink-400">Instagram Mass Posting</strong> – كل شيء تلقائي.',
    }
}

with open('translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Add new keys after nav_pricing in each language block
for lang, new_keys in new_translations.items():
    # Build the insertion text
    insertion = ''
    for key, value in new_keys.items():
        # Escape quotes in value
        value_escaped = value.replace('"', '\\"')
        insertion += f'\n        {key}: "{value_escaped}",'
    
    # Find nav_pricing and insert after it
    pattern = f'nav_pricing: "[^"]*",'
    import re
    matches = list(re.finditer(pattern, content))
    
    lang_order = ['en', 'de', 'tr', 'pt', 'es', 'ru', 'zh', 'ar']
    lang_index = lang_order.index(lang)
    
    if lang_index < len(matches):
        match = matches[lang_index]
        content = content[:match.end()] + insertion + content[match.end():]
        print(f"✓ Added hero translations to {lang}")

with open('translations.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ All hero translations added to 8 languages!")
