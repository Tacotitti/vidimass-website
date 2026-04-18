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

  // FIX 1: Replace onclick with proper event listeners
  // Remove onclick from mobile menu buttons and add them properly via JS
  const oldPattern = /<button onclick="switchLanguage\('de'\)" class="mobile-lang-btn"/g;
  const newPattern = '<button class="mobile-lang-btn" data-lang="de"';
  html = html.replace(oldPattern, newPattern);

  const oldPattern2 = /<button onclick="switchLanguage\('en'\)" class="mobile-lang-btn"/g;
  const newPattern2 = '<button class="mobile-lang-btn" data-lang="en"';
  html = html.replace(oldPattern2, newPattern2);

  // FIX 2: Add proper event listeners AFTER menu is created
  // Find the mobile menu script and add event listener setup
  const mobileMenuScriptEnd = 'for(var i=0;i<links.length;i++){';
  
  if (html.includes(mobileMenuScriptEnd)) {
    const eventListenerCode = `
  // Language switcher event listeners
  setTimeout(function() {
    var langBtns = menu.querySelectorAll('.mobile-lang-btn');
    langBtns.forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        var lang = this.getAttribute('data-lang');
        if (window.i18n && window.i18n.switchLanguage) {
          window.i18n.switchLanguage(lang);
        }
        menu.classList.remove('active');
        ov.classList.remove('active');
      });
    });
  }, 100);
  `;
    
    html = html.replace(
      mobileMenuScriptEnd,
      eventListenerCode + mobileMenuScriptEnd
    );
  }

  fs.writeFileSync(filePath, html, 'utf8');
  console.log(`✅ Fixed ${page}`);
});

console.log('\n✅ All pages fixed!');
console.log('\nFixes applied:');
console.log('  1. Removed inline onclick (fixes burger menu)');
console.log('  2. Added proper event listeners (fixes language switching)');
console.log('  3. Added i18n initialization check');
