#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Manually add data-i18n attributes to ALL untranslated sections in social-media-charting.html
Then translate all missing keys via DeepL
"""

import sys
import os
import re
import requests
import time
from dotenv import load_dotenv

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()
DEEPL_API_KEY = os.getenv('DEEPL_API_KEY')
DEEPL_URL = "https://api.deepl.com/v2/translate"

HTML_FILE = "social-media-charting.html"
TRANSLATIONS_FILE = "translations.js"

# Manual replacements: (original_html, replacement_html_with_data-i18n)
MANUAL_REPLACEMENTS = [
    # Creation Velocity section heading
    (
        '<span class="text-4xl">⚡</span> Creation Velocity as Ranking Factor',
        '<span class="text-4xl">⚡</span> <span data-i18n="charting_velocity_title">Creation Velocity as Ranking Factor</span>'
    ),
    # Creation Velocity intro
    (
        'TikTok doesn\'t just measure total count, but <strong class="text-white">growth rate</strong>:',
        '<span data-i18n-html="charting_velocity_intro">TikTok doesn\'t just measure total count, but <strong class="text-white">growth rate</strong>:</span>'
    ),
    # Slow Burn
    (
        '<div class="text-xl font-bold text-gray-400 mb-3">🐌 Slow Burn</div>',
        '<div class="text-xl font-bold text-gray-400 mb-3" data-i18n="charting_slow_burn">🐌 Slow Burn</div>'
    ),
    (
        '<p class="text-gray-300 mb-2">100 creations/day × 30 days = 3,000 total</p>',
        '<p class="text-gray-300 mb-2" data-i18n="charting_slow_calc">100 creations/day × 30 days = 3,000 total</p>'
    ),
    (
        '<div class="text-orange-400 font-semibold">➜ Moderate Ranking</div>',
        '<div class="text-orange-400 font-semibold" data-i18n="charting_moderate_rank">➜ Moderate Ranking</div>'
    ),
    # Viral Spike
    (
        '<div class="text-xl font-bold text-violet-400 mb-3">🚀 Viral Spike</div>',
        '<div class="text-xl font-bold text-violet-400 mb-3" data-i18n="charting_viral_spike">🚀 Viral Spike</div>'
    ),
    (
        '<p class="text-gray-300 mb-2">3,000 creations in 3 days = 3,000 total</p>',
        '<p class="text-gray-300 mb-2" data-i18n="charting_viral_calc">3,000 creations in 3 days = 3,000 total</p>'
    ),
    (
        '<div class="text-green-400 font-semibold">➜ TOP TRENDING</div>',
        '<div class="text-green-400 font-semibold" data-i18n="charting_top_trending">➜ TOP TRENDING</div>'
    ),
    # Why current trends
    (
        '💡 Why? TikTok wants to push <em>current</em> trends, not old ones.',
        '<span data-i18n-html="charting_why_current">💡 Why? TikTok wants to push <em>current</em> trends, not old ones.</span>'
    ),
    
    # Creator Tier Weighting section
    (
        '<span class="text-4xl">👥</span> Creator Tier Weighting',
        '<span class="text-4xl">👥</span> <span data-i18n="charting_tier_title">Creator Tier Weighting</span>'
    ),
    (
        '<p class="text-gray-300 text-lg mb-6">Not all creations are equal:</p>',
        '<p class="text-gray-300 text-lg mb-6" data-i18n="charting_tier_intro">Not all creations are equal:</p>'
    ),
    # Table headers
    (
        '<th class="py-3 px-4 text-violet-400 font-semibold">Creator Type</th>',
        '<th class="py-3 px-4 text-violet-400 font-semibold" data-i18n="charting_table_creator">Creator Type</th>'
    ),
    (
        '<th class="py-3 px-4 text-violet-400 font-semibold">Followers</th>',
        '<th class="py-3 px-4 text-violet-400 font-semibold" data-i18n="charting_table_followers">Followers</th>'
    ),
    (
        '<th class="py-3 px-4 text-violet-400 font-semibold">Algorithm Weight</th>',
        '<th class="py-3 px-4 text-violet-400 font-semibold" data-i18n="charting_table_weight">Algorithm Weight</th>'
    ),
    # Table rows
    (
        '<td class="py-3 px-4 font-semibold">Mega-Influencer</td>',
        '<td class="py-3 px-4 font-semibold" data-i18n="charting_tier_mega">Mega-Influencer</td>'
    ),
    (
        '<td class="py-3 px-4 font-semibold">Macro-Influencer</td>',
        '<td class="py-3 px-4 font-semibold" data-i18n="charting_tier_macro">Macro-Influencer</td>'
    ),
    (
        '<td class="py-3 px-4 font-semibold">Micro-Influencer</td>',
        '<td class="py-3 px-4 font-semibold" data-i18n="charting_tier_micro">Micro-Influencer</td>'
    ),
    (
        '<td class="py-3 px-4 font-semibold">Normal Users</td>',
        '<td class="py-3 px-4 font-semibold" data-i18n="charting_tier_normal">Normal Users</td>'
    ),
    # Charli note
    (
        '💡 One Charli D\'Amelio creation = 50 normal user creations (algorithmically)',
        '<span data-i18n="charting_charli_note">💡 One Charli D\'Amelio creation = 50 normal user creations (algorithmically)</span>'
    ),
    
    # Auto-Activated Features
    (
        'Auto-Activated Features',
        '<span data-i18n="charting_features_title">Auto-Activated Features</span>'
    ),
    (
        'At high creation counts, TikTok automatically activates:',
        '<span data-i18n="charting_features_intro">At high creation counts, TikTok automatically activates:</span>'
    ),
    (
        '"Use This Sound" button becomes more prominent',
        '<span data-i18n="charting_feature_sound">"Use This Sound" button becomes more prominent</span>'
    ),
    (
        '"Similar Sounds" suggestions',
        '<span data-i18n="charting_feature_similar">"Similar Sounds" suggestions</span>'
    ),
    (
        'Push notifications to users',
        '<span data-i18n="charting_feature_push">Push notifications to users</span>'
    ),
    (
        '"Trending Sounds" badge',
        '<span data-i18n="charting_feature_badge">"Trending Sounds" badge</span>'
    ),
    (
        'Spotify/Apple Music link integration (at 10,000+ creations)',
        '<span data-i18n="charting_feature_spotify">Spotify/Apple Music link integration (at 10,000+ creations)</span>'
    ),
    
    # Critical Thresholds
    (
        '<span class="text-4xl">📊</span> Critical Thresholds',
        '<span class="text-4xl">📊</span> <span data-i18n="charting_thresholds_title">Critical Thresholds</span>'
    ),
    (
        '<div class="font-semibold text-white">Starting</div>',
        '<div class="font-semibold text-white" data-i18n="charting_threshold_starting">Starting</div>'
    ),
    (
        '<div class="text-gray-400 text-sm">Normal ranking</div>',
        '<div class="text-gray-400 text-sm" data-i18n="charting_threshold_normal">Normal ranking</div>'
    ),
    (
        '<div class="font-semibold text-white">Growing</div>',
        '<div class="font-semibold text-white" data-i18n="charting_threshold_growing">Growing</div>'
    ),
    (
        '<div class="text-gray-400 text-sm">+20% FYP probability</div>',
        '<div class="text-gray-400 text-sm" data-i18n="charting_threshold_fyp">+20% FYP probability</div>'
    ),
    (
        '<div class="font-semibold text-white">Popular</div>',
        '<div class="font-semibold text-white" data-i18n="charting_threshold_popular">Popular</div>'
    ),
    (
        '<div class="text-pink-400 text-sm">"Trending Sounds" eligibility</div>',
        '<div class="text-pink-400 text-sm" data-i18n="charting_threshold_eligible">"Trending Sounds" eligibility</div>'
    ),
    (
        '<div class="font-semibold text-white">Viral</div>',
        '<div class="font-semibold text-white" data-i18n="charting_threshold_viral">Viral</div>'
    ),
    (
        '<div class="text-green-400 text-sm">Top 100 Trending, Playlist features</div>',
        '<div class="text-green-400 text-sm" data-i18n="charting_threshold_top100">Top 100 Trending, Playlist features</div>'
    ),
    (
        '<div class="font-semibold text-white">Megahit</div>',
        '<div class="font-semibold text-white" data-i18n="charting_threshold_megahit">Megahit</div>'
    ),
    (
        '<div class="text-yellow-400 text-sm">Mainstream media attention, label deals</div>',
        '<div class="text-yellow-400 text-sm" data-i18n="charting_threshold_mainstream">Mainstream media attention, label deals</div>'
    ),
    
    # Timing section
    (
        '<h3 class="text-xl font-bold text-white mb-3">⏱️ Timing Is Critical</h3>',
        '<h3 class="text-xl font-bold text-white mb-3" data-i18n="charting_timing_title">⏱️ Timing Is Critical</h3>'
    ),
    (
        '<strong class="text-white">0-72 hours:</strong> First 1,000 creations determine viral potential',
        '<span data-i18n-html="charting_timing_72h"><strong class="text-white">0-72 hours:</strong> First 1,000 creations determine viral potential</span>'
    ),
    (
        '<strong class="text-white">Week 1:</strong> 10,000+ creations = song becomes "unstoppable"',
        '<span data-i18n-html="charting_timing_week1"><strong class="text-white">Week 1:</strong> 10,000+ creations = song becomes "unstoppable"</span>'
    ),
    (
        '<strong class="text-white">Month 1:</strong> If momentum fades, algorithm deprioritizes the song',
        '<span data-i18n-html="charting_timing_month1"><strong class="text-white">Month 1:</strong> If momentum fades, algorithm deprioritizes the song</span>'
    ),
    
    # Real-World Example
    (
        '<span class="text-4xl">💡</span> Real-World Example',
        '<span class="text-4xl">💡</span> <span data-i18n="charting_example_title">Real-World Example</span>'
    ),
    (
        'Lil Nas X - "Old Town Road" (2019)',
        '<span data-i18n="charting_example_song">Lil Nas X - "Old Town Road" (2019)</span>'
    ),
    (
        '5,000 Creations (Dance Challenge)',
        '<span data-i18n="charting_example_5k">5,000 Creations (Dance Challenge)</span>'
    ),
    (
        'TikTok Trending #1',
        '<span data-i18n="charting_example_trending">TikTok Trending #1</span>'
    ),
    (
        'Spotify Viral Charts',
        '<span data-i18n="charting_example_spotify">Spotify Viral Charts</span>'
    ),
    (
        'Billboard #1 (17 weeks)',
        '<span data-i18n="charting_example_billboard">Billboard #1 (17 weeks)</span>'
    ),
    (
        '🎯 Result: Song became a world hit <strong class="text-violet-400">completely through TikTok creations</strong>, NOT through radio/label push.',
        '<span data-i18n-html="charting_example_result">🎯 Result: Song became a world hit <strong class="text-violet-400">completely through TikTok creations</strong>, NOT through radio/label push.</span>'
    ),
    
    # MediaMass Advantage
    (
        '🚀 Why MediaMass Is The Game-Changer',
        '<span data-i18n="charting_mediamass_title">🚀 Why MediaMass Is The Game-Changer</span>'
    ),
    (
        '✅ With MediaMass',
        '<span data-i18n="charting_with_mediamass">✅ With MediaMass</span>'
    ),
    (
        '250,000 creations in 24 hours',
        '<span data-i18n="charting_mediamass_250k">250,000 creations in 24 hours</span>'
    ),
    (
        'Instant algorithm threshold breach',
        '<span data-i18n="charting_mediamass_instant">Instant algorithm threshold breach</span>'
    ),
    (
        'Guaranteed trending status',
        '<span data-i18n="charting_mediamass_guaranteed">Guaranteed trending status</span>'
    ),
    (
        'Spotify/Apple Music explosion',
        '<span data-i18n="charting_mediamass_spotify">Spotify/Apple Music explosion</span>'
    ),
    (
        'Proven data for label deals',
        '<span data-i18n="charting_mediamass_proven">Proven data for label deals</span>'
    ),
    
    (
        '❌ Traditional Method',
        '<span data-i18n="charting_traditional_title">❌ Traditional Method</span>'
    ),
    (
        'Hope for organic virality (0.001% chance)',
        '<span data-i18n="charting_traditional_hope">Hope for organic virality (0.001% chance)</span>'
    ),
    (
        'Slow growth over weeks/months',
        '<span data-i18n="charting_traditional_slow">Slow growth over weeks/months</span>'
    ),
    (
        'No control over timing',
        '<span data-i18n="charting_traditional_control">No control over timing</span>'
    ),
    (
        'Algorithm might never notice',
        '<span data-i18n="charting_traditional_notice">Algorithm might never notice</span>'
    ),
    (
        'Lost momentum = lost opportunity',
        '<span data-i18n="charting_traditional_lost">Lost momentum = lost opportunity</span>'
    ),
    
    # SoundOn section (German!)
    (
        'TikTok SoundOn Engagement Rankings',
        '<span data-i18n="charting_soundon_title">TikTok SoundOn Engagement Rankings</span>'
    ),
    (
        '<strong class="text-white">Track Engagement Formel:</strong>',
        '<strong class="text-white" data-i18n="charting_soundon_formula">Track Engagement Formel:</strong>'
    ),
    (
        'Für alle Videos, die von Creators veröffentlicht wurden, die deinen Track verwenden.',
        '<span data-i18n="charting_soundon_desc">Für alle Videos, die von Creators veröffentlicht wurden, die deinen Track verwenden.</span>'
    ),
    (
        '<span class="text-yellow-400">⚠️ Mindestanforderung: Videoansichten &gt; 5.000</span>',
        '<span class="text-yellow-400" data-i18n="charting_soundon_requirement">⚠️ Mindestanforderung: Videoansichten > 5.000</span>'
    ),
    (
        '<div class="font-bold text-purple-400 mb-1">HERVORRAGEND</div>',
        '<div class="font-bold text-purple-400 mb-1" data-i18n="charting_soundon_excellent">HERVORRAGEND</div>'
    ),
    (
        '<div class="font-bold text-blue-400 mb-1">GROSSARTIG</div>',
        '<div class="font-bold text-blue-400 mb-1" data-i18n="charting_soundon_great">GROSSARTIG</div>'
    ),
    (
        '<div class="font-bold text-green-400 mb-1">GUT</div>',
        '<div class="font-bold text-green-400 mb-1" data-i18n="charting_soundon_good">GUT</div>'
    ),
    (
        '<div class="font-bold text-yellow-400 mb-1">OK</div>',
        '<div class="font-bold text-yellow-400 mb-1" data-i18n="charting_soundon_ok">OK</div>'
    ),
    (
        '<div class="font-bold text-gray-400 mb-1">FAIR</div>',
        '<div class="font-bold text-gray-400 mb-1" data-i18n="charting_soundon_fair">FAIR</div>'
    ),
    (
        '<strong class="text-violet-400">💡 MediaMass Vorteil:</strong> Mit 250.000 Videos garantieren wir, dass dein Track die <strong class="text-white">5.000 Views-Schwelle</strong> massiv überschreitet und in die <strong class="text-purple-400">Top 10% (Hervorragend)</strong> Rankings katapultiert wird!',
        '<span data-i18n-html="charting_soundon_advantage"><strong class="text-violet-400">💡 MediaMass Vorteil:</strong> Mit 250.000 Videos garantieren wir, dass dein Track die <strong class="text-white">5.000 Views-Schwelle</strong> massiv überschreitet und in die <strong class="text-purple-400">Top 10% (Hervorragend)</strong> Rankings katapultiert wird!</span>'
    ),
    
    # Final CTA
    (
        'Don\'t hope for viral success — <span class="text-violet-400">engineer it.</span>',
        '<span data-i18n-html="charting_final_cta">Don\'t hope for viral success — <span class="text-violet-400">engineer it.</span></span>'
    ),
]

print("=" * 80)
print("ADDING data-i18n ATTRIBUTES TO HTML")
print("=" * 80)

# Read HTML
with open(HTML_FILE, 'r', encoding='utf-8') as f:
    html = f.read()

# Apply replacements
replacements_made = 0
for old, new in MANUAL_REPLACEMENTS:
    if old in html:
        html = html.replace(old, new, 1)  # Replace only first occurrence
        replacements_made += 1
        print(f"✓ Replaced: {old[:60]}...")
    else:
        print(f"✗ NOT FOUND: {old[:60]}...")

# Write updated HTML
with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n{replacements_made}/{len(MANUAL_REPLACEMENTS)} replacements successful")
print("\n✅ HTML updated with data-i18n attributes!")
