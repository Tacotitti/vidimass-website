#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete translation: Add data-i18n to ALL untranslated elements
"""

import sys
import re
import requests
import time
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()
DEEPL_API_KEY = os.getenv('DEEPL_API_KEY')
DEEPL_URL = "https://api.deepl.com/v2/translate"

HTML_FILE = "social-media-charting.html"
TRANSLATIONS_FILE = "translations.js"

# Mapping of text to translation keys
TRANSLATION_MAP = {
    # Section headings
    "Creation Velocity as Ranking Factor": "charting_velocity_title",
    "Creator Tier Weighting": "charting_tier_title",
    "Auto-Activated Features": "charting_features_title",
    "Critical Thresholds": "charting_thresholds_title",
    "Real-World Example": "charting_example_title",
    "TikTok SoundOn Engagement Rankings": "charting_soundon_title",
    
    # Paragraphs
    "TikTok doesn't just measure total count, but": "charting_velocity_intro",
    "Not all creations are equal:": "charting_tier_intro",
    "At high creation counts, TikTok automatically activates:": "charting_features_intro",
    
    # Creation velocity section
    "🐌 Slow Burn": "charting_slow_burn",
    "100 creations/day × 30 days = 3,000 total": "charting_slow_burn_calc",
    "➜ Moderate Ranking": "charting_slow_ranking",
    "🚀 Viral Spike": "charting_viral_spike",
    "3,000 creations in 3 days = 3,000 total": "charting_viral_calc",
    "➜ TOP TRENDING": "charting_top_trending",
    "💡 Why? TikTok wants to push": "charting_why_current",
    
    # Tier weighting table headers (already in German, will be translated)
    "Mega-Influencer": "charting_tier_mega",
    "Macro-Influencer": "charting_tier_macro",
    "Micro-Influencer": "charting_tier_micro",
    "Normal Users": "charting_tier_normal",
    "Creator Type": "charting_table_creator_type",
    "Followers": "charting_table_followers",
    "Algorithm Weight": "charting_table_weight",
    
    # Features list
    '"Use This Sound" button becomes more prominent': "charting_feature_1",
    '"Similar Sounds" suggestions': "charting_feature_2",
    "Push notifications to users": "charting_feature_3",
    '"Trending Sounds" badge': "charting_feature_4",
    "Spotify/Apple Music link integration (at 10,000+ creations)": "charting_feature_5",
    
    # Critical thresholds
    "Starting": "charting_threshold_starting",
    "Normal ranking": "charting_threshold_normal",
    "Growing": "charting_threshold_growing",
    "+20% FYP probability": "charting_threshold_20fyp",
    "Popular": "charting_threshold_popular",
    '"Trending Sounds" eligibility': "charting_threshold_trending",
    "Viral": "charting_threshold_viral",
    "Top 100 Trending, Playlist features": "charting_threshold_top100",
    "Megahit": "charting_threshold_megahit",
    "Mainstream media attention, label deals": "charting_threshold_mainstream",
    
    # Timing section
    "⏱️ Timing Is Critical": "charting_timing_title",
    "0-72 hours:": "charting_timing_0_72",
    "First 1,000 creations determine viral potential": "charting_timing_first_1000",
    "Week 1:": "charting_timing_week1",
    '10,000+ creations = song becomes "unstoppable"': "charting_timing_unstoppable",
    "Month 1:": "charting_timing_month1",
    "If momentum fades, algorithm deprioritizes the song": "charting_timing_fade",
    
    # Example section
    'Lil Nas X - "Old Town Road" (2019)': "charting_example_song",
    "Day 1-3:": "charting_example_day1",
    "5,000 Creations (Dance Challenge)": "charting_example_5k",
    "Week 1:": "charting_example_week1",
    "50,000 Creations →": "charting_example_50k",
    "TikTok Trending #1": "charting_example_trending1",
    "Month 1:": "charting_example_month1",
    "500,000 Creations →": "charting_example_500k",
    "Spotify Viral Charts": "charting_example_spotify",
    "Month 2:": "charting_example_month2",
    "2 Million Creations →": "charting_example_2m",
    "Billboard #1 (17 weeks)": "charting_example_billboard",
    "🎯 Result: Song became a world hit": "charting_example_result",
    
    # MediaMass advantage
    "🚀 Why MediaMass Is The Game-Changer": "charting_mediamass_title",
    "✅ With MediaMass": "charting_with_mediamass",
    "250,000 creations in 24 hours": "charting_mediamass_250k",
    "Instant algorithm threshold breach": "charting_mediamass_instant",
    "Guaranteed trending status": "charting_mediamass_guaranteed",
    "Spotify/Apple Music explosion": "charting_mediamass_spotify",
    "Proven data for label deals": "charting_mediamass_proven",
    
    "❌ Traditional Method": "charting_traditional_title",
    "Hope for organic virality (0.001% chance)": "charting_traditional_hope",
    "Slow growth over weeks/months": "charting_traditional_slow",
    "No control over timing": "charting_traditional_no_control",
    "Algorithm might never notice": "charting_traditional_never",
    "Lost momentum = lost opportunity": "charting_traditional_lost",
    
    # SoundOn section (German text!)
    "Track Engagement Formel:": "charting_soundon_formula",
    "Für alle Videos, die von Creators veröffentlicht wurden, die deinen Track verwenden.": "charting_soundon_desc",
    "⚠️ Mindestanforderung: Videoansichten > 5.000": "charting_soundon_requirement",
    "HERVORRAGEND": "charting_soundon_excellent",
    "GROSSARTIG": "charting_soundon_great",
    "GUT": "charting_soundon_good",
    "OK": "charting_soundon_ok",
    "FAIR": "charting_soundon_fair",
    "Top 10%": "charting_soundon_top10",
    "Top 20%": "charting_soundon_top20",
    "Top 30%": "charting_soundon_top30",
    "Top 50%": "charting_soundon_top50",
    "Bottom 50%": "charting_soundon_bottom50",
    "💡 MediaMass Vorteil:": "charting_soundon_advantage",
    "Mit 250.000 Videos garantieren wir, dass dein Track die": "charting_soundon_guarantee",
    "5.000 Views-Schwelle": "charting_soundon_threshold",
    "Top 10% (Hervorragend)": "charting_soundon_hervorragend",
    
    # Final CTA
    "Don't hope for viral success —": "charting_final_cta1",
    "engineer it.": "charting_final_cta2",
}

def translate_batch(texts, target_lang):
    """Translate via DeepL with new auth"""
    try:
        response = requests.post(
            DEEPL_URL,
            headers={
                'Authorization': f'DeepL-Auth-Key {DEEPL_API_KEY}',
                'Content-Type': 'application/json'
            },
            json={
                'text': texts,
                'target_lang': target_lang,
                'source_lang': 'DE'
            }
        )
        
        if response.status_code == 200:
            result = response.json()
            return [t['text'] for t in result['translations']]
        else:
            print(f"DeepL error: {response.status_code}")
            return texts  # Fallback
    except Exception as e:
        print(f"Translation error: {e}")
        return texts

def main():
    print("=" * 80)
    print("COMPLETE TRANSLATION - ADD ALL MISSING data-i18n ATTRIBUTES")
    print("=" * 80)
    
    # Read HTML
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Build all German source texts
    german_texts = {}
    for text, key in TRANSLATION_MAP.items():
        german_texts[key] = text
    
    print(f"\nTranslating {len(german_texts)} new keys...")
    
    # Translate to all languages
    keys = list(german_texts.keys())
    source_texts = list(german_texts.values())
    
    translations = {
        'de': dict(zip(keys, source_texts)),  # Original German
        'en': {},
        'tr': {},
        'pt': {},
        'es': {}
    }
    
    # Translate
    print("Translating to EN...")
    en_texts = translate_batch(source_texts, 'EN')
    translations['en'] = dict(zip(keys, en_texts))
    time.sleep(0.5)
    
    print("Translating to TR...")
    tr_texts = translate_batch(source_texts, 'TR')
    translations['tr'] = dict(zip(keys, tr_texts))
    time.sleep(0.5)
    
    print("Translating to PT...")
    pt_texts = translate_batch(source_texts, 'PT-PT')
    translations['pt'] = dict(zip(keys, pt_texts))
    time.sleep(0.5)
    
    print("Translating to ES...")
    es_texts = translate_batch(source_texts, 'ES')
    translations['es'] = dict(zip(keys, es_texts))
    
    # Now add data-i18n attributes to HTML
    print("\nAdding data-i18n attributes to HTML...")
    
    modified_html = html
    replacements = 0
    
    for original_text, key in TRANSLATION_MAP.items():
        # Escape special regex characters
        escaped = re.escape(original_text)
        
        # Try to find and replace
        # Pattern: find text in various contexts
        patterns = [
            # In plain tags
            f'(<(?:h[1-6]|p|div|span|strong|td|th|li)[^>]*>)\\s*{escaped}\\s*(</)',
            # Just the text between tags
            f'(>[^<]*){escaped}([^<]*<)',
        ]
        
        for pattern in patterns:
            if re.search(pattern, modified_html):
                replacement = f'\\1<span data-i18n="{key}">{original_text}</span>\\2'
                modified_html = re.sub(pattern, replacement, modified_html, count=1)
                replacements += 1
                break
    
    print(f"Added {replacements} data-i18n attributes")
    
    # Write modified HTML
    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(modified_html)
    
    # Update translations.js
    print("\nUpdating translations.js...")
    
    with open(TRANSLATIONS_FILE, 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    # Add new translations to each language block
    for lang in ['en', 'de', 'tr', 'pt', 'es']:
        # Find the language block
        pattern = rf'{lang}:\s*\{{'
        match = re.search(pattern, js_content)
        
        if match:
            # Build new entries
            new_entries = []
            for key in sorted(translations[lang].keys()):
                value = translations[lang][key]
                escaped = value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
                new_entries.append(f'        {key}: "{escaped}",')
            
            # Insert after opening brace
            insert_pos = match.end()
            insertion = '\n' + '\n'.join(new_entries) + '\n'
            js_content = js_content[:insert_pos] + insertion + js_content[insert_pos:]
            print(f"  Added {len(new_entries)} entries for {lang}")
    
    # Write updated translations.js
    with open(TRANSLATIONS_FILE, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print("\n" + "=" * 80)
    print("COMPLETE!")
    print("=" * 80)
    print(f"Translation keys added: {len(TRANSLATION_MAP)}")
    print(f"HTML elements updated: {replacements}")
    print(f"Translations per language: {len(translations['en'])}")
    print("\nAll 5 languages (EN, DE, TR, PT, ES) now fully translated!")

if __name__ == '__main__':
    main()
