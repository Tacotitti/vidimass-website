const fs = require('fs');
const path = require('path');

// Read files
const preispath = path.join(__dirname, 'preisliste.html');
const contactPath = path.join(__dirname, 'contact.html');
const dePath = path.join(__dirname, 'translations', 'de.json');
const enPath = path.join(__dirname, 'translations', 'en.json');

let preisliste = fs.readFileSync(preispath, 'utf8');
let contact = fs.readFileSync(contactPath, 'utf8');
let de = JSON.parse(fs.readFileSync(dePath, 'utf8'));
let en = JSON.parse(fs.readFileSync(enPath, 'utf8'));

// Initialize pricing keys if not exist
if (!de.pricing) de.pricing = {};
if (!en.pricing) en.pricing = {};

// TikTok pricing translations
const tiktokPricing = {
  row1_videos: { de: "1.000 Videos", en: "1,000 Videos" },
  row1_price: { de: "$79", en: "$79" },
  row1_per: { de: "~$0,079", en: "~$0.079" },
  
  row2_videos: { de: "5.000 Videos", en: "5,000 Videos" },
  row2_price: { de: "$199", en: "$199" },
  row2_per: { de: "~$0,040", en: "~$0.040" },
  
  row3_videos: { de: "15.000 Videos", en: "15,000 Videos" },
  row3_price: { de: "$399", en: "$399" },
  row3_per: { de: "~$0,027", en: "~$0.027" },
  
  row4_videos: { de: "30.000 Videos", en: "30,000 Videos" },
  row4_price: { de: "$749", en: "$749" },
  row4_per: { de: "~$0,025", en: "~$0.025" },
  row4_badge: { de: "BELIEBT", en: "POPULAR" },
  
  row5_videos: { de: "60.000 Videos", en: "60,000 Videos" },
  row5_price: { de: "$1.299", en: "$1,299" },
  row5_per: { de: "~$0,022", en: "~$0.022" },
  
  row6_videos: { de: "125.000 Videos", en: "125,000 Videos" },
  row6_price: { de: "$2.199", en: "$2,199" },
  row6_per: { de: "~$0,018", en: "~$0.018" },
  
  row7_videos: { de: "250.000 Videos", en: "250,000 Videos" },
  row7_price: { de: "$3.999", en: "$3,999" },
  row7_per: { de: "~$0,016", en: "~$0.016" },
  row7_badge: { de: "BESTES ANGEBOT", en: "BEST VALUE" },
  
  row8_videos: { de: "500.000 Videos", en: "500,000 Videos" },
  row8_price: { de: "$6.999", en: "$6,999" },
  row8_per: { de: "~$0,014", en: "~$0.014" },
  
  row9_videos: { de: "1.000.000 Videos", en: "1,000,000 Videos" },
  row9_price: { de: "$11.999", en: "$11,999" },
  row9_per: { de: "~$0,012", en: "~$0.012" },
  
  cta: { de: "Jetzt Anfragen", en: "Get Started" },
  custom_title: { de: "Individuelle Pakete", en: "Custom Packages" },
  custom_desc: { de: "Brauchen Sie mehr? Wir erstellen individuelle Pakete für Ihre spezifischen Anforderungen.", en: "Need more? We create custom packages for your specific requirements." },
  custom_cta: { de: "Kontakt aufnehmen", en: "Contact Us" }
};

// Add to translation files
if (!de.pricing.tiktok) de.pricing.tiktok = {};
if (!en.pricing.tiktok) en.pricing.tiktok = {};

Object.keys(tiktokPricing).forEach(key => {
  de.pricing.tiktok[key] = tiktokPricing[key].de;
  en.pricing.tiktok[key] = tiktokPricing[key].en;
});

// Instagram pricing (same structure)
if (!de.pricing.instagram) de.pricing.instagram = {};
if (!en.pricing.instagram) en.pricing.instagram = {};

Object.keys(tiktokPricing).forEach(key => {
  de.pricing.instagram[key] = tiktokPricing[key].de;
  en.pricing.instagram[key] = tiktokPricing[key].en;
});

// Save translation files
fs.writeFileSync(dePath, JSON.stringify(de, null, 2), 'utf8');
fs.writeFileSync(enPath, JSON.stringify(en, null, 2), 'utf8');

console.log('✅ Added ~60 pricing translation keys to de.json and en.json');
console.log('\n📝 Now manually add data-i18n attributes to preisliste.html table cells');
console.log('   Example: <td data-i18n="pricing.tiktok.row1_videos">1,000 Videos</td>');
