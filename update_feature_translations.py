import re

with open('translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

# New description for all languages
new_descriptions = {
    'en': "Personalized hashtags and video comments in every upload for maximum viral push. Our AI engine generates unique #tags and captions that optimally trigger TikTok's recommendation system and multiply organic reach.",
    'de': "Personalisierte Hashtags und Video-Kommentare in jedem Upload für maximalen viralen Push. Unsere KI-Engine generiert unique #Tags und Captions, die TikToks Recommendation-System optimal triggern und organische Reichweite multiplizieren.",
    'tr': "Her yüklemede maksimum viral etki için kişiselleştirilmiş hashtagler ve video yorumları. AI motorumuz, TikTok'un öneri sistemini optimal tetikleyen ve organik erişimi çoğaltan benzersiz #taglar ve altyazılar üretir.",
    'pt': "Hashtags personalizadas e comentários de vídeo em cada upload para máximo impulso viral. Nosso motor de IA gera #tags e legendas únicas que acionam otimamente o sistema de recomendação do TikTok e multiplicam o alcance orgânico.",
    'es': "Hashtags personalizados y comentarios de video en cada carga para máximo impulso viral. Nuestro motor de IA genera #tags y subtítulos únicos que activan óptimamente el sistema de recomendación de TikTok y multiplican el alcance orgánico.",
    'ru': "Персонализированные хэштеги и комментарии к видео в каждой загрузке для максимального вирусного эффекта. Наш ИИ-движок генерирует уникальные #теги и подписи, которые оптимально активируют систему рекомендаций TikTok и умножают органический охват.",
    'zh': "每次上传都有个性化标签和视频评论，实现最大病毒式传播。我们的 AI 引擎生成独特的 #标签和标题，最优触发 TikTok 推荐系统并倍增有机覆盖。",
    'ar': "هاشتاجات مخصصة وتعليقات فيديو في كل تحميل لأقصى دفع فيروسي. محرك الذكاء الاصطناعي لدينا ينتج #علامات وتسميات فريدة تحفز بشكل مثالي نظام توصيات TikTok وتضاعف الوصول العضوي."
}

# Replace each feature_1_desc (match old pattern and replace)
old_pattern = r'(feature_1_desc:\s*")[^"]*(")'

# Find language sections and replace appropriately
sections = [
    ('en', 'English'),
    ('de', 'German'),
    ('tr', 'Turkish'),
    ('pt', 'Portuguese'),
    ('es', 'Spanish'),
    ('ru', 'Russian'),
    ('zh', 'Chinese'),
    ('ar', 'Arabic')
]

for lang_code, lang_name in sections:
    new_desc = new_descriptions[lang_code]
    # Find and replace the old description with new one
    # Use non-greedy match to replace each occurrence
    content = re.sub(
        r'(feature_1_desc:\s*")[^"]*(")',
        f'\\1{new_desc}\\2',
        content,
        count=1
    )
    print(f"✓ Updated {lang_name} ({lang_code})")

with open('translations.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ All 8 languages updated!")
