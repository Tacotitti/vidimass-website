const fs = require('fs');
const path = require('path');

// Pages to update
const pages = [
  'index.html',
  'preisliste.html',
  'contact.html',
  'social-media-charting.html',
  'datenschutz.html',
  'nutzungsbedingungen.html'
];

// Language Switcher HTML for Desktop (in navigation)
const desktopSwitcher = `
                    <!-- Language Switcher -->
                    <div class="language-switcher flex items-center gap-2">
                        <button onclick="switchLanguage('de')" class="lang-btn px-3 py-1.5 rounded-lg transition-all hover:bg-white/10" data-lang="de">
                            <span class="text-sm font-medium">🇩🇪 DE</span>
                        </button>
                        <span class="text-gray-600">|</span>
                        <button onclick="switchLanguage('en')" class="lang-btn px-3 py-1.5 rounded-lg transition-all hover:bg-white/10" data-lang="en">
                            <span class="text-sm font-medium">🇬🇧 EN</span>
                        </button>
                    </div>
`;

// Language Switcher for Mobile Menu
const mobileSwitcher = `
    <div class="mobile-lang-switcher flex items-center justify-center gap-4 pt-6 mt-6 border-t border-white/10">
        <button onclick="switchLanguage('de')" class="mobile-lang-btn flex items-center gap-2 px-4 py-2 rounded-lg transition-all hover:bg-white/10" data-lang="de">
            <span class="text-2xl">🇩🇪</span>
            <span class="text-sm font-medium">Deutsch</span>
        </button>
        <button onclick="switchLanguage('en')" class="mobile-lang-btn flex items-center gap-2 px-4 py-2 rounded-lg transition-all hover:bg-white/10" data-lang="en">
            <span class="text-2xl">🇬🇧</span>
            <span class="text-sm font-medium">English</span>
        </button>
    </div>
`;

// CSS for active language button
const languageSwitcherCSS = `
/* Language Switcher Styles */
.lang-btn.active,
.mobile-lang-btn.active {
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.2) 0%, rgba(219, 39, 119, 0.2) 100%);
    border: 1px solid rgba(139, 92, 246, 0.4);
}

.lang-btn:hover,
.mobile-lang-btn:hover {
    transform: translateY(-1px);
}
`;

pages.forEach(page => {
  const filePath = path.join(__dirname, page);
  
  if (!fs.existsSync(filePath)) {
    console.log(`⚠️  ${page} not found, skipping...`);
    return;
  }

  let html = fs.readFileSync(filePath, 'utf8');

  // 1. Add desktop switcher before the "Get Started" button
  if (html.includes('class="cta-button') && !html.includes('language-switcher')) {
    html = html.replace(
      /(\s*<a href="contact\.html" class="cta-button)/,
      `${desktopSwitcher}\n$1`
    );
    console.log(`✅ Added desktop language switcher to ${page}`);
  }

  // 2. Add mobile switcher at the end of mobile menu
  if (html.includes('class="mobile-menu') && !html.includes('mobile-lang-switcher')) {
    // Find the closing </div> of mobile-menu
    const mobileMenuEnd = html.indexOf('</div><!-- Mobile Menu -->');
    if (mobileMenuEnd !== -1) {
      html = html.slice(0, mobileMenuEnd) + mobileSwitcher + '\n    ' + html.slice(mobileMenuEnd);
      console.log(`✅ Added mobile language switcher to ${page}`);
    }
  }

  // 3. Add CSS if not already present
  if (html.includes('<style>') && !html.includes('Language Switcher Styles')) {
    html = html.replace(
      '</style>',
      `${languageSwitcherCSS}\n</style>`
    );
    console.log(`✅ Added language switcher CSS to ${page}`);
  }

  // Write back
  fs.writeFileSync(filePath, html, 'utf8');
  console.log(`🎯 Updated ${page}`);
});

console.log('\n✅ All pages updated with language switcher buttons!');
console.log('\n📍 Language switchers added:');
console.log('   - Desktop: In navigation bar (before "Get Started")');
console.log('   - Mobile: At bottom of mobile menu');
console.log('\n🎨 Styled with active state highlighting');
