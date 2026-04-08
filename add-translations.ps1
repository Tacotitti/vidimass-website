# PowerShell Script: Add new translation keys to translations.js

# Read the original file
$filePath = "translations.js"
$content = Get-Content $filePath -Raw

# Define new keys to add (after existing keys, before closing brace of each language)

$newKeysEN = @'
,
        nav_pricing: "Pricing",
        pricing_badge_popular: "POPULAR",
        pricing_badge_best_value: "BEST VALUE",
        pricing_tiktok_1k: "1,000 Videos",
        pricing_tiktok_5k: "5,000 Videos",
        pricing_tiktok_15k: "15,000 Videos",
        pricing_tiktok_30k: "30,000 Videos",
        pricing_tiktok_60k: "60,000 Videos",
        pricing_tiktok_125k: "125,000 Videos",
        pricing_tiktok_250k: "250,000 Videos",
        pricing_tiktok_500k: "500,000 Videos",
        pricing_tiktok_1m: "1,000,000 Videos",
        pricing_instagram_1k: "1,000 Reels",
        pricing_instagram_5k: "5,000 Reels",
        pricing_instagram_15k: "15,000 Reels",
        pricing_instagram_30k: "30,000 Reels",
        pricing_instagram_60k: "60,000 Reels",
        pricing_instagram_125k_plus: "125,000+ Reels",
        pricing_instagram_125k: "125,000 Reels",
        pricing_instagram_250k: "250,000 Reels",
        pricing_instagram_flat_rate: "Flat Rate",
        pricing_per_reel: "Per Reel",
        pricing_custom_volume_label: "Custom Volumes:",
        pricing_custom_volume_text: "Any quantity over 125K Reels at a flat rate price of €0.026 per Reel available",
        lang_english: "English",
        lang_german: "Deutsch",
        lang_turkish: "Türkçe",
        lang_portuguese: "Português",
        lang_spanish: "Español"
'@

$newKeysDE = @'
,
        nav_pricing: "Preisliste",
        pricing_badge_popular: "BELIEBT",
        pricing_badge_best_value: "BEST VALUE",
        pricing_tiktok_1k: "1.000 Videos",
        pricing_tiktok_5k: "5.000 Videos",
        pricing_tiktok_15k: "15.000 Videos",
        pricing_tiktok_30k: "30.000 Videos",
        pricing_tiktok_60k: "60.000 Videos",
        pricing_tiktok_125k: "125.000 Videos",
        pricing_tiktok_250k: "250.000 Videos",
        pricing_tiktok_500k: "500.000 Videos",
        pricing_tiktok_1m: "1.000.000 Videos",
        pricing_instagram_1k: "1.000 Reels",
        pricing_instagram_5k: "5.000 Reels",
        pricing_instagram_15k: "15.000 Reels",
        pricing_instagram_30k: "30.000 Reels",
        pricing_instagram_60k: "60.000 Reels",
        pricing_instagram_125k_plus: "125.000+ Reels",
        pricing_instagram_125k: "125.000 Reels",
        pricing_instagram_250k: "250.000 Reels",
        pricing_instagram_flat_rate: "Flat Rate",
        pricing_per_reel: "Pro Reel",
        pricing_custom_volume_label: "Custom Volumes:",
        pricing_custom_volume_text: "Beliebige Menge über 125K Reels zum Flat-Rate-Preis von €0.026 pro Reel verfügbar",
        lang_english: "English",
        lang_german: "Deutsch",
        lang_turkish: "Türkçe",
        lang_portuguese: "Português",
        lang_spanish: "Español"
'@

$newKeysTR = @'
,
        nav_pricing: "Fiyatlandırma",
        pricing_badge_popular: "POPÜLER",
        pricing_badge_best_value: "EN İYİ DEĞER",
        pricing_tiktok_1k: "1.000 Video",
        pricing_tiktok_5k: "5.000 Video",
        pricing_tiktok_15k: "15.000 Video",
        pricing_tiktok_30k: "30.000 Video",
        pricing_tiktok_60k: "60.000 Video",
        pricing_tiktok_125k: "125.000 Video",
        pricing_tiktok_250k: "250.000 Video",
        pricing_tiktok_500k: "500.000 Video",
        pricing_tiktok_1m: "1.000.000 Video",
        pricing_instagram_1k: "1.000 Reel",
        pricing_instagram_5k: "5.000 Reel",
        pricing_instagram_15k: "15.000 Reel",
        pricing_instagram_30k: "30.000 Reel",
        pricing_instagram_60k: "60.000 Reel",
        pricing_instagram_125k_plus: "125.000+ Reel",
        pricing_instagram_125k: "125.000 Reel",
        pricing_instagram_250k: "250.000 Reel",
        pricing_instagram_flat_rate: "Sabit Fiyat",
        pricing_per_reel: "Reel Başına",
        pricing_custom_volume_label: "Özel Hacimler:",
        pricing_custom_volume_text: "125 bin Reels'in üzerindeki herhangi bir miktar, Reel başına sabit €0.026 fiyatla mevcut",
        lang_english: "English",
        lang_german: "Deutsch",
        lang_turkish: "Türkçe",
        lang_portuguese: "Português",
        lang_spanish: "Español"
'@

$newKeysPT = @'
,
        nav_pricing: "Preços",
        pricing_badge_popular: "POPULAR",
        pricing_badge_best_value: "MELHOR VALOR",
        pricing_tiktok_1k: "1.000 Vídeos",
        pricing_tiktok_5k: "5.000 Vídeos",
        pricing_tiktok_15k: "15.000 Vídeos",
        pricing_tiktok_30k: "30.000 Vídeos",
        pricing_tiktok_60k: "60.000 Vídeos",
        pricing_tiktok_125k: "125.000 Vídeos",
        pricing_tiktok_250k: "250.000 Vídeos",
        pricing_tiktok_500k: "500.000 Vídeos",
        pricing_tiktok_1m: "1.000.000 Vídeos",
        pricing_instagram_1k: "1.000 Reels",
        pricing_instagram_5k: "5.000 Reels",
        pricing_instagram_15k: "15.000 Reels",
        pricing_instagram_30k: "30.000 Reels",
        pricing_instagram_60k: "60.000 Reels",
        pricing_instagram_125k_plus: "125.000+ Reels",
        pricing_instagram_125k: "125.000 Reels",
        pricing_instagram_250k: "250.000 Reels",
        pricing_instagram_flat_rate: "Taxa Fixa",
        pricing_per_reel: "Por Reel",
        pricing_custom_volume_label: "Volumes Personalizados:",
        pricing_custom_volume_text: "Qualquer quantidade acima de 125K Reels disponível à taxa fixa de €0,026 por Reel",
        lang_english: "English",
        lang_german: "Deutsch",
        lang_turkish: "Türkçe",
        lang_portuguese: "Português",
        lang_spanish: "Español"
'@

$newKeysES = @'
,
        nav_pricing: "Precios",
        pricing_badge_popular: "POPULAR",
        pricing_badge_best_value: "MEJOR VALOR",
        pricing_tiktok_1k: "1.000 Videos",
        pricing_tiktok_5k: "5.000 Videos",
        pricing_tiktok_15k: "15.000 Videos",
        pricing_tiktok_30k: "30.000 Videos",
        pricing_tiktok_60k: "60.000 Videos",
        pricing_tiktok_125k: "125.000 Videos",
        pricing_tiktok_250k: "250.000 Videos",
        pricing_tiktok_500k: "500.000 Videos",
        pricing_tiktok_1m: "1.000.000 Videos",
        pricing_instagram_1k: "1.000 Reels",
        pricing_instagram_5k: "5.000 Reels",
        pricing_instagram_15k: "15.000 Reels",
        pricing_instagram_30k: "30.000 Reels",
        pricing_instagram_60k: "60.000 Reels",
        pricing_instagram_125k_plus: "125.000+ Reels",
        pricing_instagram_125k: "125.000 Reels",
        pricing_instagram_250k: "250.000 Reels",
        pricing_instagram_flat_rate: "Tarifa Plana",
        pricing_per_reel: "Por Reel",
        pricing_custom_volume_label: "Volúmenes Personalizados:",
        pricing_custom_volume_text: "Cualquier cantidad superior a 125K Reels disponible a una tarifa plana de €0,026 por Reel",
        lang_english: "English",
        lang_german: "Deutsch",
        lang_turkish: "Türkçe",
        lang_portuguese: "Português",
        lang_spanish: "Español"
'@

# Pattern to find the last key before closing brace for each language
# We'll search for "why_title:" which appears to be the last key in each section

$content = $content -replace '(why_title: "Warum Mass Posting mit MediaMass\?"[\r\n]+    },[\r\n]+    [\r\n]+    de: {)', ('why_title: "Why Mass Posting with MediaMass?"' + $newKeysEN + "`r`n    },`r`n    `r`n    de: {")

# ... similar for other languages

Write-Output "Script prepared. Run manually to update translations.js"
