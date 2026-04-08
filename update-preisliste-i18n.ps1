# PowerShell script to add data-i18n attributes to preisliste.html

$file = "preisliste.html"
$content = Get-Content $file -Raw

# Navigation links
$content = $content -replace '(<a href="index.html#features"[^>]*>)Features</a>', '$1<span data-i18n="nav_features">Features</span></a>'
$content = $content -replace '(<a href="social-media-charting.html"[^>]*>)Social Media Charting</a>', '$1<span data-i18n="nav_charting">Social Media Charting</span></a>'
$content = $content -replace '(<a href="preisliste.html"[^>]*>)Preisliste</a>', '$1<span data-i18n="nav_pricing">Preisliste</span></a>'

# Badges
$content = $content -replace '(<span[^>]*>)BELIEBT</span>', '$1<span data-i18n="badge_popular">BELIEBT</span></span>'
$content = $content -replace '(<span[^>]*>)BEST VALUE</span>', '$1<span data-i18n="badge_best_value">BEST VALUE</span></span>'

# Table headers - Per Reel
$content = $content -replace '>Pro Reel</th>', ' data-i18n="pricing_table_per_reel">Pro Reel</th>'

# Flat Rate
$content = $content -replace '>Flat Rate</td>', ' data-i18n="pricing_flat_rate">Flat Rate</td>'

# Custom Volumes
$content = $content -replace '<strong>💡 Custom Volumes:</strong>', '<strong data-i18n="pricing_custom_volumes_label">💡 Custom Volumes:</strong>'
$content = $content -replace 'Beliebige Menge über 125K Reels zum Flat-Rate-Preis von 0\.026€ pro Reel verfügbar', '<span data-i18n="pricing_custom_volumes_text">Beliebige Menge über 125K Reels zum Flat-Rate-Preis von 0.026€ pro Reel verfügbar</span>'

# Video counts
$content = $content -replace '>1,000 Videos</td>', ' data-i18n="pricing_videos_1k">1,000 Videos</td>'
$content = $content -replace '>5,000 Videos</td>', ' data-i18n="pricing_videos_5k">5,000 Videos</td>'
$content = $content -replace '>15,000 Videos</td>', ' data-i18n="pricing_videos_15k">15,000 Videos</td>'
$content = $content -replace '>30,000 Videos(\s*)<span', ' data-i18n="pricing_videos_30k">30,000 Videos$1<span'
$content = $content -replace '>60,000 Videos</td>', ' data-i18n="pricing_videos_60k">60,000 Videos</td>'
$content = $content -replace '>125,000 Videos</td>', ' data-i18n="pricing_videos_125k">125,000 Videos</td>'
$content = $content -replace '>250,000 Videos(\s*)<span', ' data-i18n="pricing_videos_250k">250,000 Videos$1<span'
$content = $content -replace '>500,000 Videos</td>', ' data-i18n="pricing_videos_500k">500,000 Videos</td>'
$content = $content -replace '>1,000,000 Videos</td>', ' data-i18n="pricing_videos_1m">1,000,000 Videos</td>'

# Reels counts
$content = $content -replace '>1,000 Reels</td>', ' data-i18n="pricing_reels_1k">1,000 Reels</td>'
$content = $content -replace '>5,000 Reels</td>', ' data-i18n="pricing_reels_5k">5,000 Reels</td>'
$content = $content -replace '>15,000 Reels</td>', ' data-i18n="pricing_reels_15k">15,000 Reels</td>'
$content = $content -replace '>30,000 Reels(\s*)<span', ' data-i18n="pricing_reels_30k">30,000 Reels$1<span'
$content = $content -replace '>60,000 Reels</td>', ' data-i18n="pricing_reels_60k">60,000 Reels</td>'
$content = $content -replace '>125,000\+ Reels(\s*)<span', ' data-i18n="pricing_reels_125k_plus">125,000+ Reels$1<span'
$content = $content -replace '>125,000 Reels</td>', ' data-i18n="pricing_reels_125k">125,000 Reels</td>'
$content = $content -replace '>250,000 Reels</td>', ' data-i18n="pricing_reels_250k">250,000 Reels</td>'

# Footer - add Impressum if missing
if ($content -notmatch 'footer_imprint') {
    $content = $content -replace '(<a href="datenschutz\.html")', '<a href="impressum.html" class="hover:text-white transition-colors" data-i18n="footer_imprint">Impressum</a>$1'
}

Set-Content $file $content -NoNewline
Write-Host "✅ preisliste.html updated with data-i18n attributes"
