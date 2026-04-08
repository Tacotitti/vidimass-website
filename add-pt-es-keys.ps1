# PowerShell script to add translation keys to PT and ES sections

$newKeysPT = @"
        
        // Additional keys for complete coverage (2026-04-07)
        badge_popular: "POPULAR",
        badge_best_value: "MELHOR VALOR",
        pricing_table_per_reel: "Por Reel",
        pricing_flat_rate: "Taxa Fixa",
        pricing_custom_volumes_label: "💡 Volumes Personalizados:",
        pricing_custom_volumes_text: "Qualquer quantidade acima de 125K Reels disponível a uma taxa fixa de €0,026 por Reel",
        footer_imprint: "Imprensa",
        pricing_videos_1k: "1.000 Vídeos",
        pricing_videos_5k: "5.000 Vídeos",
        pricing_videos_15k: "15.000 Vídeos",
        pricing_videos_30k: "30.000 Vídeos",
        pricing_videos_60k: "60.000 Vídeos",
        pricing_videos_125k: "125.000 Vídeos",
        pricing_videos_250k: "250.000 Vídeos",
        pricing_videos_500k: "500.000 Vídeos",
        pricing_videos_1m: "1.000.000 Vídeos",
        pricing_reels_1k: "1.000 Reels",
        pricing_reels_5k: "5.000 Reels",
        pricing_reels_15k: "15.000 Reels",
        pricing_reels_30k: "30.000 Reels",
        pricing_reels_60k: "60.000 Reels",
        pricing_reels_125k_plus: "125.000+ Reels",
        pricing_reels_125k: "125.000 Reels",
        pricing_reels_250k: "250.000 Reels"
"@

$newKeysES = @"
        
        // Additional keys for complete coverage (2026-04-07)
        badge_popular: "POPULAR",
        badge_best_value: "MEJOR VALOR",
        pricing_table_per_reel: "Por Reel",
        pricing_flat_rate: "Tarifa Plana",
        pricing_custom_volumes_label: "💡 Volúmenes Personalizados:",
        pricing_custom_volumes_text: "Cualquier cantidad superior a 125K Reels disponible a una tarifa fija de €0,026 por Reel",
        footer_imprint: "Aviso Legal",
        pricing_videos_1k: "1.000 Videos",
        pricing_videos_5k: "5.000 Videos",
        pricing_videos_15k: "15.000 Videos",
        pricing_videos_30k: "30.000 Videos",
        pricing_videos_60k: "60.000 Videos",
        pricing_videos_125k: "125.000 Videos",
        pricing_videos_250k: "250.000 Videos",
        pricing_videos_500k: "500.000 Videos",
        pricing_videos_1m: "1.000.000 Videos",
        pricing_reels_1k: "1.000 Reels",
        pricing_reels_5k: "5.000 Reels",
        pricing_reels_15k: "15.000 Reels",
        pricing_reels_30k: "30.000 Reels",
        pricing_reels_60k: "60.000 Reels",
        pricing_reels_125k_plus: "125.000+ Reels",
        pricing_reels_125k: "125.000 Reels",
        pricing_reels_250k: "250.000 Reels"
"@

Write-Output "PT Keys:`n$newKeysPT"
Write-Output "`nES Keys:`n$newKeysES"
