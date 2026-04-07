#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fixes translations.js by reading it properly and replacing only the exact values
"""

import re

def fix_translations():
    with open('translations.js', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    replacements = {
        'charting_hero_title1:': '        charting_hero_title1: "Wie Mass Posting",\n',
        'charting_hero_title2:': '        charting_hero_title2: "Viralen Erfolg Antreibt",\n',
        'charting_hero_subtitle:': '        charting_hero_subtitle: "Die Wissenschaft hinter TikToks Algorithmus und warum Creation Velocity der ultimative Growth Hack für Musiker ist",\n',
        'charting_intro_heading:': '        charting_intro_heading: "🎵 Warum Video Creations Alles Sind",\n',
        'charting_intro_text:': '        charting_intro_text: "Video Creations (User-Generated Content mit deinem Song) sind <strong class=\\"text-white\\">der wichtigste Ranking-Faktor</strong> für musikalischen Erfolg auf TikTok. Hier ist die technische Aufschlüsselung, wie TikToks Algorithmus funktioniert und warum Mass Posting das Spiel verändert.",\n',
        'charting_algorithm_heading:': '        charting_algorithm_heading: "TikToks Algorithmus: 3 Phasen",\n',
        'charting_phase1_heading:': '        charting_phase1_heading: "Phase 1: Initialer Test-Pool",\n',
        'charting_phase1_bullet1:': '        charting_phase1_bullet1: "Neues Creation-Video wird 300-500 zufälligen Usern gezeigt",\n',
        'charting_phase1_bullet2:': '        charting_phase1_bullet2: "Wenn Engagement-Rate > 8% → geht zu Phase 2",\n',
        'charting_phase1_bullet3:': '        charting_phase1_bullet3: "Wenn < 8% → Video stirbt",\n',
        'charting_phase2_heading:': '        charting_phase2_heading: "Phase 2: Interest Graph Expansion",\n',
        'charting_phase2_bullet1:': '        charting_phase2_bullet1: "Video wird Usern gezeigt, die ähnliche Sounds/Hashtags mögen",\n',
        'charting_phase2_bullet2:': '        charting_phase2_bullet2: "Mit jedem positiven Signal (Like, Share, Creation) → breitere Verteilung",\n',
        'charting_phase2_bullet3:': '        charting_phase2_bullet3: "Songs mit vielen Creations haben höhere Startchance in Phase 2",\n',
        'charting_phase3_heading:': '        charting_phase3_heading: "Phase 3: Virale Explosion",\n',
        'charting_phase3_bullet1:': '        charting_phase3_bullet1: "Wenn kritische Schwellenwerte überschritten werden (z.B. 10.000 Creations in 24h)",\n',
        'charting_phase3_bullet2:': '        charting_phase3_bullet2: "TikTok aktiviert \\"Viral Push\\" Mechanismus",\n',
        'charting_phase3_bullet3:': '        charting_phase3_bullet3: "Song wird aktiv in \\"Trending Sounds\\" Sektion gepusht",\n',
    }
    
    in_de_section = False
    fixed_count = 0
    
    for i, line in enumerate(lines):
        # Track wenn wir in der DE-Sektion sind
        if '    de: {' in line:
            in_de_section = True
            print(f"✅ Gefunden: DE-Sektion bei Zeile {i+1}")
        elif in_de_section and line.strip().startswith('},'):
            in_de_section = False
            print(f"✅ Ende der DE-Sektion bei Zeile {i+1}")
        
        # Nur in der DE-Sektion ersetzen
        if in_de_section:
            for key, new_line in replacements.items():
                if key in line:
                    lines[i] = new_line
                    fixed_count += 1
                    print(f"✅ Fixed Zeile {i+1}: {key}")
                    break
    
    # Schreibe zurück
    with open('translations.js', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"\n✅ {fixed_count} Zeilen gefixt!")
    return fixed_count

if __name__ == "__main__":
    print("🔧 Starte Line-by-Line Fix...\n")
    fixed = fix_translations()
    
    if fixed > 0:
        import subprocess
        print("\n🔍 Teste Syntax...")
        result = subprocess.run(['node', '-c', 'translations.js'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ SYNTAX OK!")
        else:
            print(f"❌ SYNTAX ERROR:\n{result.stderr[:500]}")
