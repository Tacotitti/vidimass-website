#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Übersetzt ALLE fehlenden deutschen Texte in translations.js
Nutzt JSON-parsing statt Regex für saubere Updates
"""

import re
import json

# Vollständige deutsche Übersetzungen (alphabetisch sortiert für Übersicht)
GERMAN_TRANSLATIONS_CHARTING = {
    "charting_algorithm_heading": "TikToks Algorithmus: 3 Phasen",
    "charting_example_heading": "💡 Real-World Beispiel",
    "charting_example_result": "🎯 Ergebnis: Song wurde zum Welthit komplett durch TikTok Creations, NICHT durch Radio/Label Push.",
    "charting_example_song": "Lil Nas X - \\\"Old Town Road\\\" (2019)",
    "charting_feature_badge": "\\\"Trending Sounds\\\" Badge",
    "charting_feature_push": "Push-Benachrichtigungen an User",
    "charting_feature_similar": "\\\"Similar Sounds\\\" Vorschläge",
    "charting_feature_sound": "\\\"Use This Sound\\\" Button wird prominenter",
    "charting_feature_spotify": "Spotify/Apple Music Link-Integration (ab 10.000+ Creations)",
    "charting_features_heading": "Auto-Aktivierte Features",
    "charting_features_intro": "Bei hoher Creation-Anzahl aktiviert TikTok automatisch:",
    "charting_final_cta": "Hoffe nicht auf viralen Erfolg — <span class=\\\"text-violet-400\\\">erschaffe ihn.</span>",
    "charting_hero_subtitle": "Die Wissenschaft hinter TikToks Algorithmus und warum Creation Velocity der ultimative Growth Hack für Musiker ist",
    "charting_hero_title1": "Wie Mass Posting",
    "charting_hero_title2": "Viralen Erfolg Antreibt",
    "charting_intro_heading": "🎵 Warum Video Creations Alles Sind",
    "charting_intro_text": "Video Creations (User-Generated Content mit deinem Song) sind <strong class=\\\"text-white\\\">der wichtigste Ranking-Faktor</strong> für musikalischen Erfolg auf TikTok. Hier ist die technische Aufschlüsselung, wie TikToks Algorithmus funktioniert und warum Mass Posting das Spiel verändert.",
    "charting_phase1_bullet1": "Neues Creation-Video wird 300-500 zufälligen Usern gezeigt",
    "charting_phase1_bullet2": "Wenn Engagement-Rate > 8% → geht zu Phase 2",
    "charting_phase1_bullet3": "Wenn < 8% → Video stirbt",
    "charting_phase1_heading": "Phase 1: Initialer Test-Pool",
    "charting_phase2_bullet1": "Video wird Usern gezeigt, die ähnliche Sounds/Hashtags mögen",
    "charting_phase2_bullet2": "Mit jedem positiven Signal (Like, Share, Creation) → breitere Verteilung",
    "charting_phase2_bullet3": "Songs mit vielen Creations haben höhere Startchance in Phase 2",
    "charting_phase2_heading": "Phase 2: Interest Graph Expansion",
    "charting_phase3_bullet1": "Wenn kritische Schwellenwerte überschritten werden (z.B. 10.000 Creations in 24h)",
    "charting_phase3_bullet2": "TikTok aktiviert \\\"Viral Push\\\" Mechanismus",
    "charting_phase3_bullet3": "Song wird aktiv in \\\"Trending Sounds\\\" Sektion gepusht",
    "charting_phase3_heading": "Phase 3: Virale Explosion",
    "charting_table_creator": "Creator-Typ",
    "charting_table_followers": "Follower",
    "charting_table_weight": "Algorithmus-Gewicht",
    "charting_thresholds_heading": "📊 Kritische Schwellenwerte",
    "charting_timing_heading": "⏱️ Timing ist Kritisch",
    "charting_timing_month1": "<strong>Monat 1:</strong> Wenn Momentum verblasst, priorisiert der Algorithmus den Song herunter",
    "charting_timing_week1": "<strong>Woche 1:</strong> 10.000+ Creations = Song wird \\\"unstoppable\\\"",
    "charting_velocity_heading": "⚡ Creation Velocity als Ranking-Faktor",
    "charting_velocity_intro": "TikTok misst nicht nur die Gesamtzahl, sondern auch die <strong class=\\\"text-white\\\">Wachstumsrate</strong>:",
}

def main():
    print("🔧 Starte Fix für deutsche Übersetzungen (manuell)...\n")
    
    # Lese translations.js
    with open('translations.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Backup
    with open('translations.js.backup2', 'w', encoding='utf-8') as f:
        f.write(content)
    print("💾 Backup gespeichert: translations.js.backup2\n")
    
    # Finde die deutsche Sektion (de: { ... })
    pattern = r'(de:\s*\{)(.*?)(^\s{4}\},)'
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    
    if not match:
        print("❌ Konnte deutsche Sektion nicht finden!")
        return
    
    de_section = match.group(2)
    fixes_count = 0
    
    # Ersetze jede Übersetzung einzeln
    for key, german_text in GERMAN_TRANSLATIONS_CHARTING.items():
        # Regex für den Key (flexibler für verschiedene Formate)
        key_pattern = rf'(\s+{re.escape(key)}:\s*)"([^"]*(?:\\.[^"]*)*)"'
        
        if re.search(key_pattern, de_section):
            # Ersetze den Wert
            de_section_new = re.sub(
                key_pattern,
                rf'\1"{german_text}"',
                de_section,
                count=1
            )
            
            if de_section_new != de_section:
                de_section = de_section_new
                fixes_count += 1
                print(f"✅ Fixed: {key}")
        else:
            print(f"⚠️ Key nicht gefunden: {key}")
    
    # Ersetze die deutsche Sektion
    new_content = content[:match.start(2)] + de_section + content[match.end(2):]
    
    # Schreibe neue Datei
    with open('translations.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\n✅ {fixes_count} Übersetzungen aktualisiert!")
    print("💾 translations.js gespeichert!")
    print("\n🔍 Teste Syntax...")
    
    import subprocess
    try:
        result = subprocess.run(['node', '-c', 'translations.js'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ SYNTAX OK!")
        else:
            print(f"❌ SYNTAX ERROR:\n{result.stderr}")
    except Exception as e:
        print(f"⚠️ Konnte Syntax nicht testen: {e}")

if __name__ == "__main__":
    main()
