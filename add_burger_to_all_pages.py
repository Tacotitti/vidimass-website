import os
import re

# Pages to update (exclude index.html as it already has it)
pages = [
    'preisliste.html',
    'contact.html',
    'tiktok-charting.html',
    'datenschutz.html',
    'nutzungsbedingungen.html'
]

# Burger button HTML
burger_button = '''                <button class="md:hidden mobile-menu-toggle text-white">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>'''

# Script tags to add before </body>
script_tags = '''
    <!-- Scripts -->
    <script src="script.js"></script>
    <script src="language.js"></script>
    <script src="translations.js"></script>
</body>'''

for page in pages:
    if not os.path.exists(page):
        print(f"Skip {page} (not found)")
        continue
        
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add burger button after the desktop nav closing </div>
    # Find pattern: </div>\n            </div>\n        </div>\n    </nav>
    pattern = r'(</div>\s*</div>\s*</div>\s*</nav>)'
    if 'mobile-menu-toggle' not in content:
        replacement = burger_button + '\n            \\1'
        content = re.sub(pattern, replacement, content, count=1)
        print(f"✓ Added burger button to {page}")
    else:
        print(f"- Burger button already exists in {page}")
    
    # 2. Add scripts before </body>
    if 'script.js' not in content:
        content = content.replace('</body>', script_tags)
        print(f"✓ Added scripts to {page}")
    else:
        print(f"- Scripts already exist in {page}")
    
    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)

print("\n✅ Done - All pages updated with burger menu + scripts")
