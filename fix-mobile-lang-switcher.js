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

// Language switcher HTML to inject into mobile menu
const languageSwitcherHTML = `<div class="mobile-lang-switcher" style="display:flex;align-items:center;justify-content:center;gap:12px;padding-top:24px;margin-top:24px;border-top:1px solid rgba(255,255,255,0.1)"><button onclick="switchLanguage('de')" class="mobile-lang-btn" data-lang="de" style="display:flex;align-items:center;gap:8px;padding:10px 16px;border-radius:8px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#fff;font-size:14px;font-weight:500;cursor:pointer;transition:all 0.2s"><span style="font-size:20px">🇩🇪</span><span>Deutsch</span></button><button onclick="switchLanguage('en')" class="mobile-lang-btn" data-lang="en" style="display:flex;align-items:center;gap:8px;padding:10px 16px;border-radius:8px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#fff;font-size:14px;font-weight:500;cursor:pointer;transition:all 0.2s"><span style="font-size:20px">🇬🇧</span><span>English</span></button></div>`;

pages.forEach(page => {
  const filePath = path.join(__dirname, page);
  
  if (!fs.existsSync(filePath)) {
    console.log(`⚠️  ${page} not found, skipping...`);
    return;
  }

  let html = fs.readFileSync(filePath, 'utf8');

  // Find the mobile menu innerHTML assignment
  const menuInnerHTMLPattern = /(menu\.innerHTML\s*=\s*')([^']+)(';)/;
  
  if (menuInnerHTMLPattern.test(html)) {
    // Check if language switcher already exists
    if (!html.includes('mobile-lang-switcher')) {
      html = html.replace(menuInnerHTMLPattern, (match, p1, p2, p3) => {
        // Add language switcher at the end of the menu HTML
        return p1 + p2 + languageSwitcherHTML + p3;
      });
      
      fs.writeFileSync(filePath, html, 'utf8');
      console.log(`✅ Added mobile language switcher to ${page}`);
    } else {
      console.log(`ℹ️  ${page} already has mobile language switcher`);
    }
  } else {
    console.log(`⚠️  Could not find mobile menu innerHTML in ${page}`);
  }
});

console.log('\n✅ Mobile language switcher added to all pages!');
console.log('\n📱 Test on mobile:');
console.log('   1. Open burger menu');
console.log('   2. Scroll to bottom');
console.log('   3. See 🇩🇪 Deutsch | 🇬🇧 English buttons');
