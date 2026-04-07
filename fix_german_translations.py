#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Findet und übersetzt fehlende deutsche Übersetzungen in translations.js
"""

import re
import json

# Deutsche Übersetzungen für die Charting-Seite
GERMAN_TRANSLATIONS = {
    # Hero Section
    "charting_hero_title1": "Wie Mass Posting",
    "charting_hero_title2": "Viralen Erfolg Antreibt",
    "charting_hero_subtitle": "Die Wissenschaft hinter TikToks Algorithmus und warum Creation Velocity der ultimative Growth Hack für Musiker ist",
    
    # Intro
    "charting_intro_heading": "🎵 Warum Video Creations Alles Sind",
    "charting_intro_text": "Video Creations (User-Generated Content mit deinem Song) sind <strong class=\"text-white\">der wichtigste Ranking-Faktor</strong> für musikalischen Erfolg auf TikTok. Hier ist die technische Aufschlüsselung, wie TikToks Algorithmus funktioniert und warum Mass Posting das Spiel verändert.",
    
    # Algorithm Heading
    "charting_algorithm_heading": "TikToks Algorithmus: 3 Phasen",
    
    # Phase 1
    "charting_phase1_heading": "Phase 1: Initialer Test-Pool",
    "charting_phase1_bullet1": "Neues Creation-Video wird 300-500 zufälligen Usern gezeigt",
    "charting_phase1_bullet2": "Wenn Engagement-Rate > 8% → geht zu Phase 2",
    "charting_phase1_bullet3": "Wenn < 8% → Video stirbt",
    
    # Phase 2
    "charting_phase2_heading": "Phase 2: Interest Graph Expansion",
    "charting_phase2_bullet1": "Video wird Usern gezeigt, die ähnliche Sounds/Hashtags mögen",
    "charting_phase2_bullet2": "Mit jedem positiven Signal (Like, Share, Creation) → breitere Verteilung",
    "charting_phase2_bullet3": "Songs mit vielen Creations haben höhere Startchance in Phase 2",
    
    # Phase 3
    "charting_phase3_heading": "Phase 3: Virale Explosion",
    "charting_phase3_bullet1": "Wenn kritische Schwellenwerte überschritten werden (z.B. 10.000 Creations in 24h)",
    "charting_phase3_bullet2": "TikTok aktiviert \"Viral Push\" Mechanismus",
    "charting_phase3_bullet3": "Song wird aktiv in \"Trending Sounds\" Sektion gepusht",
    
    # Creation Velocity
    "charting_velocity_heading": "⚡ Creation Velocity als Ranking-Faktor",
    "charting_velocity_intro": "TikTok misst nicht nur die Gesamtzahl, sondern auch die <strong class=\"text-white\">Wachstumsrate</strong>:",
    "charting_velocity_slow_title": "🐌 Slow Burn",
    "charting_velocity_slow_calc": "100 Creations/Tag × 30 Tage = 3.000 gesamt",
    "charting_velocity_slow_result": "➜ Moderate Ranking",
    "charting_velocity_viral_title": "🚀 Viraler Spike",
    "charting_velocity_viral_calc": "3.000 Creations in 3 Tagen = 3.000 gesamt",
    "charting_velocity_viral_result": "➜ TOP TRENDING",
    "charting_velocity_why": "💡 Warum? TikTok will <em>aktuelle</em> Trends pushen, nicht alte.",
    
    # Creator Tier
    "charting_creator_heading": "👥 Creator-Tier Gewichtung",
    "charting_creator_intro": "Nicht alle Creations sind gleich:",
    "charting_table_creator": "Creator-Typ",
    "charting_table_followers": "Follower",
    "charting_table_weight": "Algorithmus-Gewicht",
    "charting_creator_mega": "Mega-Influencer",
    "charting_creator_macro": "Macro-Influencer",
    "charting_creator_micro": "Micro-Influencer",
    "charting_creator_normal": "Normale User",
    "charting_creator_note": "💡 Eine Charli D'Amelio Creation = 50 normale User Creations (algorithmisch)",
    
    # Auto-Activated Features
    "charting_features_heading": "Auto-Aktivierte Features",
    "charting_features_intro": "Bei hoher Creation-Anzahl aktiviert TikTok automatisch:",
    "charting_feature_sound": "\"Use This Sound\" Button wird prominenter",
    "charting_feature_similar": "\"Similar Sounds\" Vorschläge",
    "charting_feature_push": "Push-Benachrichtigungen an User",
    "charting_feature_badge": "\"Trending Sounds\" Badge",
    "charting_feature_spotify": "Spotify/Apple Music Link-Integration (ab 10.000+ Creations)",
    
    # Critical Thresholds
    "charting_thresholds_heading": "📊 Kritische Schwellenwerte",
    "charting_threshold_100": "100",
    "charting_threshold_100_label": "Starting",
    "charting_threshold_100_desc": "Normales Ranking",
    "charting_threshold_1k": "1.000",
    "charting_threshold_1k_label": "Growing",
    "charting_threshold_1k_desc": "+20% FYP Wahrscheinlichkeit",
    "charting_threshold_10k": "10.000",
    "charting_threshold_10k_label": "Popular",
    "charting_threshold_10k_desc": "\"Trending Sounds\" Berechtigung",
    "charting_threshold_50k": "50.000",
    "charting_threshold_50k_label": "Viral",
    "charting_threshold_50k_desc": "Top 100 Trending, Playlist Features",
    "charting_threshold_100k": "100.000+",
    "charting_threshold_100k_label": "Megahit",
    "charting_threshold_100k_desc": "Mainstream Media Aufmerksamkeit, Label Deals",
    
    # Timing
    "charting_timing_heading": "⏱️ Timing ist Kritisch",
    "charting_timing_0_72h": "<strong>0-72 Stunden:</strong> Erste 1.000 Creations bestimmen virales Potenzial",
    "charting_timing_week1": "<strong>Woche 1:</strong> 10.000+ Creations = Song wird \"unstoppable\"",
    "charting_timing_month1": "<strong>Monat 1:</strong> Wenn Momentum verblasst, priorisiert der Algorithmus den Song herunter",
    
    # Real-World Example
    "charting_example_heading": "💡 Real-World Beispiel",
    "charting_example_song": "Lil Nas X - \"Old Town Road\" (2019)",
    "charting_example_day1": "Tag 1-3:",
    "charting_example_5k": "5.000 Creations (Dance Challenge)",
    "charting_example_week1": "Woche 1:",
    "charting_example_50k": "50.000 Creations → <span class=\"text-violet-400\">TikTok Trending #1</span>",
    "charting_example_month1": "Monat 1:",
    "charting_example_500k": "500.000 Creations → <span class=\"text-pink-400\">Spotify Viral Charts</span>",
    "charting_example_month2": "Monat 2:",
    "charting_example_2m": "2 Millionen Creations → <span class=\"text-yellow-400\">Billboard #1 (17 Wochen)</span>",
    "charting_example_result": "🎯 Ergebnis: Song wurde zum Welthit <strong>komplett durch TikTok Creations</strong>, NICHT durch Radio/Label Push.",
    
    # MediaMass Advantage
    "charting_advantage_heading": "🚀 Warum MediaMass Der Game-Changer Ist",
    "charting_advantage_with": "✅ Mit MediaMass",
    "charting_advantage_with_bullet1": "250.000 Creations in 24 Stunden",
    "charting_advantage_with_bullet2": "Sofortiger Algorithmus-Schwellenwert-Durchbruch",
    "charting_advantage_with_bullet3": "Garantierter Trending-Status",
    "charting_advantage_with_bullet4": "Spotify/Apple Music Explosion",
    "charting_advantage_with_bullet5": "Bewährte Daten für Label Deals",
    "charting_advantage_without": "❌ Traditionelle Methode",
    "charting_advantage_without_bullet1": "Hoffnung auf organische Viralität (0,001% Chance)",
    "charting_advantage_without_bullet2": "Langsames Wachstum über Wochen/Monate",
    "charting_advantage_without_bullet3": "Keine Kontrolle über Timing",
    "charting_advantage_without_bullet4": "Algorithmus bemerkt es vielleicht nie",
    "charting_advantage_without_bullet5": "Verlorenes Momentum = verlorene Chance",
    
    # SoundOn Rankings
    "charting_soundon_heading": "📊 TikTok SoundOn Engagement Rankings",
    "charting_soundon_formula": "Track Engagement Formel:",
    "charting_soundon_desc": "Für alle Videos, die von Creators veröffentlicht wurden, die deinen Track verwenden.",
    "charting_soundon_warning": "⚠️ Mindestanforderung: Videoansichten > 5.000",
    "charting_soundon_excellent": "HERVORRAGEND",
    "charting_soundon_excellent_desc": "Top 10%",
    "charting_soundon_great": "GROSSARTIG",
    "charting_soundon_great_desc": "Top 20%",
    "charting_soundon_good": "GUT",
    "charting_soundon_good_desc": "Top 30%",
    "charting_soundon_ok": "OK",
    "charting_soundon_ok_desc": "Top 50%",
    "charting_soundon_fair": "FAIR",
    "charting_soundon_fair_desc": "Bottom 50%",
    "charting_soundon_advantage": "<strong class=\"text-violet-400\">💡 MediaMass Vorteil:</strong> Mit 250.000 Videos garantieren wir, dass dein Track die <strong class=\"text-white\">5.000 Views-Schwelle</strong> massiv überschreitet und in die <strong class=\"text-purple-400\">Top 10% (Hervorragend)</strong> Rankings katapultiert wird!",
    
    # Final CTA
    "charting_final_cta": "Hoffe nicht auf viralen Erfolg — <span class=\"text-violet-400\">erschaffe ihn.</span>",
    "charting_cta_button": "Jetzt starten",
}

def read_translations_file():
    """Liest die translations.js Datei"""
    with open('translations.js', 'r', encoding='utf-8') as f:
        return f.read()

def update_german_section(content):
    """Aktualisiert die deutsche Sektion mit korrekten Übersetzungen"""
    
    # Finde die deutsche Sektion (de: { ... })
    pattern = r'(de:\s*\{)(.*?)(^\s{4}\},)'
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    
    if not match:
        print("❌ Konnte deutsche Sektion nicht finden!")
        return content
    
    start_pos = match.start(2)
    end_pos = match.end(2)
    de_section = match.group(2)
    
    # Zähle Fixes
    fixes_count = 0
    
    # Ersetze jede fehlende/falsche Übersetzung
    for key, german_text in GERMAN_TRANSLATIONS.items():
        # Suche nach dem Key in der deutschen Sektion
        key_pattern = rf'(\s+{re.escape(key)}:\s*)"([^"]*)"'
        key_match = re.search(key_pattern, de_section)
        
        if key_match:
            old_value = key_match.group(2)
            # Prüfe ob es eine englische Übersetzung ist (grobe Heuristik)
            if old_value != german_text:
                # Ersetze
                de_section = re.sub(
                    key_pattern,
                    rf'\1"{german_text}"',
                    de_section,
                    count=1
                )
                fixes_count += 1
                print(f"✅ Fixed: {key}")
                print(f"   Alt: {old_value[:60]}...")
                print(f"   Neu: {german_text[:60]}...")
        else:
            print(f"⚠️ Key nicht gefunden: {key}")
    
    # Ersetze die deutsche Sektion im gesamten Content
    new_content = content[:start_pos] + de_section + content[end_pos:]
    
    print(f"\n✅ {fixes_count} Übersetzungen aktualisiert!")
    return new_content

def main():
    print("🔧 Starte Fix für deutsche Übersetzungen...\n")
    
    # Lese translations.js
    content = read_translations_file()
    
    # Aktualisiere deutsche Sektion
    new_content = update_german_section(content)
    
    # Speichere Backup
    with open('translations.js.backup', 'w', encoding='utf-8') as f:
        f.write(content)
    print("\n💾 Backup gespeichert: translations.js.backup")
    
    # Schreibe neue Datei
    with open('translations.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("💾 translations.js aktualisiert!")
    
    print("\n✅ FERTIG! Teste jetzt die Website im Browser.")

if __name__ == "__main__":
    main()
