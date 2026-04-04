import re

with open('translations.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Define new descriptions for all languages
updates = {
    # English (line ~39)
    'en': "Personalized hashtags and video comments in every upload for maximum viral push. Our AI engine generates unique #tags and captions that optimally trigger TikTok's recommendation system and multiply organic reach.",
    # German (line ~135)
    'de': "Personalisierte Hashtags und Video-Kommentare in jedem Upload für maximalen viralen Push. Unsere KI-Engine generiert unique #Tags und Captions, die TikToks Recommendation-System optimal triggern und organische Reichweite multiplizieren.",
    # Turkish
    'tr': "Her yüklemede maksimum viral etki için kişiselleştirilmiş hashtagler ve video yorumları. AI motorumuz, TikTok'un öneri sistemini optimal tetikleyen ve organik erişimi çoğaltan benzersiz #taglar ve altyazılar üretir.",
    # Portuguese
    'pt': "Hashtags personalizadas e comentários de vídeo em cada upload para máximo impulso viral. Nosso motor de IA gera #tags e legendas únicas que acionam otimamente o sistema de recomendação do TikTok e multiplicam o alcance orgânico.",
    # Spanish
    'es': "Hashtags personalizados y comentarios de video en cada carga para máximo impulso viral. Nuestro motor de IA genera #tags y subtítulos únicos que activan óptimamente el sistema de recomendación de TikTok y multiplican el alcance orgánico.",
    # Russian
    'ru': "Персонализированные хэштеги и комментарии к видео в каждой загрузке для максимального вирусного эффекта. Наш ИИ-движок генерирует уникальные #теги и подписи, которые оптимально активируют систему рекомендаций TikTok и умножают органический охват.",
    # Chinese
    'zh': "每次上传都有个性化标签和视频评论，实现最大病毒式传播。我们的 AI 引擎生成独特的 #标签和标题，最优触发 TikTok 推荐系统并倍增有机覆盖。",
    # Arabic
    'ar': "هاشتاجات مخصصة وتعليقات فيديو في كل تحميل لأقصى دفع فيروسي. محرك الذكاء الاصطناعي لدينا ينتج #علامات وتسميات فريدة تحفز بشكل مثالي نظام توصيات TikTok وتضاعف الوصول العضوي."
}

# Find and replace each feature_1_desc line
updated_count = 0
for i, line in enumerate(lines):
    if 'feature_1_desc:' in line and updated_count < 8:
        # Extract current description
        match = re.search(r'feature_1_desc:\s*"([^"]*)"', line)
        if match:
            # Determine which language based on position
            lang_map = {
                0: 'en',
                1: 'de', 
                2: 'tr',
                3: 'pt',
                4: 'es',
                5: 'ru',
                6: 'zh',
                7: 'ar'
            }
            lang = lang_map.get(updated_count)
            if lang:
                new_desc = updates[lang]
                # Replace the line
                indent = len(line) - len(line.lstrip())
                lines[i] = ' ' * indent + f'feature_1_desc: "{new_desc}",\n'
                print(f"✓ Updated {lang} (line {i+1})")
                updated_count += 1

with open('translations.js', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"\n✅ Updated {updated_count} languages!")
