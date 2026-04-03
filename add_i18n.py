import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add scripts before </body>
scripts_to_add = '''
    <!-- Language System -->
    <script src="translations.js"></script>
    <script src="language.js"></script>
'''

html = html.replace('<!-- JavaScript -->', scripts_to_add + '\n    <!-- JavaScript -->')

# Add data-i18n attributes
replacements = [
    # Navigation
    (r'<a href="#features" class="nav-link[^>]*>Features</a>', r'<a href="#features" class="nav-link text-gray-300 hover:text-white transition-colors" data-i18n="nav_features">Features</a>'),
    (r'<a href="#stats" class="nav-link[^>]*>Stats</a>', r'<a href="#stats" class="nav-link text-gray-300 hover:text-white transition-colors" data-i18n="nav_stats">Stats</a>'),
    (r'<a href="#packages" class="nav-link[^>]*>Packages</a>', r'<a href="#packages" class="nav-link text-gray-300 hover:text-white transition-colors" data-i18n="nav_packages">Packages</a>'),
    (r'Get Started\s*</button>', r'<span data-i18n="nav_get_started">Get Started</span></button>'),
    
    # Hero badge
    (r'<span class="text-sm text-gray-300">24/7 Distribution Active</span>', r'<span class="text-sm text-gray-300" data-i18n="hero_badge">24/7 Distribution Active</span>'),
    
    # Hero titles
    (r'<span class="bg-gradient-to-r from-violet-400 via-fuchsia-400 to-pink-400 bg-clip-text text-transparent">\s*Mass Video Posting\s*</span>', r'<span class="bg-gradient-to-r from-violet-400 via-fuchsia-400 to-pink-400 bg-clip-text text-transparent" data-i18n="hero_title_1">Mass Video Posting</span>'),
    (r'<br>\s*<span class="text-white">At Scale</span>', r'<br>\n                    <span class="text-white" data-i18n="hero_title_2">At Scale</span>'),
    
    # Hero subtitle
    (r'<p class="text-xl md:text-2xl text-gray-300 mb-12[^>]*>.*?Distribute up to.*?</p>', r'<p class="text-xl md:text-2xl text-gray-300 mb-12 max-w-3xl mx-auto leading-relaxed" data-i18n="hero_subtitle">Distribute up to <span class="font-bold text-violet-400">250,000 videos daily</span> across TikTok, Instagram, and multiple platforms with enterprise-grade automation.</p>', re.DOTALL),
    
    # Hero CTAs
    (r'Get Started Now\s*</button>', r'<span data-i18n="hero_cta_primary">Get Started Now</span></button>'),
    (r'View Packages\s*</button>', r'<span data-i18n="hero_cta_secondary">View Packages</span></button>'),
    
    # Trust indicators
    (r'<span>Enterprise Security</span>', r'<span data-i18n="hero_trust_1">Enterprise Security</span>'),
    (r'<span>99\.9% Uptime</span>', r'<span data-i18n="hero_trust_2">99.9% Uptime</span>'),
    (r'<span>24/7 Support</span>', r'<span data-i18n="hero_trust_3">24/7 Support</span>'),
]

for pattern, replacement in replacements:
    html = re.sub(pattern, replacement, html, flags=re.DOTALL)

# Write the updated HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML updated successfully!")
