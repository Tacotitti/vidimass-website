const fs = require('fs');
const path = require('path');

const pages = [
  'index.html',
  'preisliste.html',
  'contact.html',
  'social-media-charting.html',
  'datenschutz.html',
  'nutzungsbedingungen.html'
];

pages.forEach(page => {
  const filePath = path.join(__dirname, page);
  
  if (!fs.existsSync(filePath)) {
    console.log(`⚠️  ${page} not found, skipping...`);
    return;
  }

  let html = fs.readFileSync(filePath, 'utf8');

  // Remove ALL onclick="switchLanguage(...)" from desktop buttons
  html = html.replace(/onclick="switchLanguage\('de'\)"/g, '');
  html = html.replace(/onclick="switchLanguage\('en'\)"/g, '');

  // Add event listener script for desktop language switcher (before </body>)
  const desktopListenerScript = `
    <script>
    // Desktop Language Switcher Event Listeners
    document.addEventListener('DOMContentLoaded', function() {
        // Wait for i18n to be ready
        function setupLanguageSwitchers() {
            var desktopBtns = document.querySelectorAll('.language-switcher .lang-btn');
            desktopBtns.forEach(function(btn) {
                btn.addEventListener('click', function(e) {
                    e.preventDefault();
                    var lang = this.getAttribute('data-lang');
                    if (window.i18n && window.i18n.switchLanguage) {
                        window.i18n.switchLanguage(lang);
                    } else {
                        console.warn('i18n not ready yet, retrying...');
                        setTimeout(function() {
                            if (window.i18n && window.i18n.switchLanguage) {
                                window.i18n.switchLanguage(lang);
                            }
                        }, 500);
                    }
                });
            });
        }
        
        // Try immediately and retry if needed
        setTimeout(setupLanguageSwitchers, 100);
    });
    </script>
`;

  // Add before </body> if not already there
  if (!html.includes('Desktop Language Switcher Event Listeners')) {
    html = html.replace('</body>', desktopListenerScript + '\n</body>');
    console.log(`✅ Added desktop event listeners to ${page}`);
  }

  fs.writeFileSync(filePath, html, 'utf8');
  console.log(`✅ Fixed ${page}`);
});

console.log('\n🎯 All pages fixed!');
console.log('\nChanges:');
console.log('  ✅ Removed ALL inline onclick attributes');
console.log('  ✅ Added proper event listeners for desktop');
console.log('  ✅ Added i18n ready check with retry logic');
console.log('  ✅ Mobile menu already fixed in previous step');
