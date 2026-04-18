# 🌍 MediaMass i18n Translation System

## Quick Overview

This is a lightweight, SEO-optimized, multilingual translation system for masspost.store built for Cloudflare Pages.

### ✨ Features
- 🇩🇪 **German** + 🇬🇧 **English** (easily expandable)
- 🔍 **SEO-friendly** (hreflang tags, dynamic meta tags, canonical URLs)
- 🚀 **Fast** (~50ms initialization, 5KB translation files)
- 📱 **Mobile-first** (responsive language switcher)
- 💾 **Persistent** (localStorage + URL parameters)
- 🎯 **Auto-detection** (browser language, URL, localStorage)
- ✅ **Zero dependencies** (vanilla JavaScript)
- 🛡️ **Secure** (XSS-safe, CSP-compatible)

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Include i18n.js
```html
<!-- Add before </head> in your HTML -->
<script src="i18n.js"></script>
</head>
```

### Step 2: Add Translation Keys
```html
<!-- Example: Navigation -->
<a href="contact.html" data-i18n="nav.contact">Contact</a>

<!-- Example: Heading -->
<h1 data-i18n="hero.title">Welcome</h1>

<!-- Example: Button -->
<button data-i18n="cta.button">Get Started</button>
```

### Step 3: Create Translation Files
Create `translations/de.json` and `translations/en.json`:

```json
{
  "nav": {
    "contact": "Kontakt"
  },
  "hero": {
    "title": "Willkommen"
  },
  "cta": {
    "button": "Jetzt starten"
  }
}
```

### Step 4: Test Locally
```bash
# Start local server
python -m http.server 8000

# Open browser
http://localhost:8000?lang=de
```

**Done!** 🎉

---

## 📖 Usage

### Basic Translation
```html
<!-- Text content -->
<div data-i18n="key.path">Fallback text</div>

<!-- Placeholder -->
<input type="text" data-i18n="form.email" placeholder="Email">

<!-- HTML content -->
<div data-i18n-html="key.with.html">
  <!-- Allows HTML in translation -->
</div>

<!-- Aria label -->
<button data-i18n-aria="button.close" aria-label="Close">X</button>

<!-- Title attribute -->
<abbr data-i18n-title="tooltip.info" title="Info">ℹ️</abbr>
```

### JavaScript API
```javascript
// Get current language
window.i18n.getCurrentLanguage(); // 'de' or 'en'

// Switch language
window.i18n.switchLanguage('en');

// Get translation
window.i18n.t('nav.contact'); // "Contact"

// Listen for language changes
window.addEventListener('languageChanged', (e) => {
    console.log('New language:', e.detail.lang);
});
```

---

## 🎨 Language Switcher

The system automatically creates a language switcher in your navigation.

### Desktop Switcher
Added automatically to `.hidden.md\:flex` navigation container:
```
[DE] | [EN]
```

### Mobile Switcher
Added automatically to `.mobile-menu`:
```
🇩🇪 Deutsch    🇬🇧 English
```

### Customization
Style via CSS:
```css
.language-switcher .lang-switch-btn {
    /* Your styles */
}

.language-switcher .lang-switch-btn.active {
    background: linear-gradient(to right, #7c3aed, #ec4899);
    color: white;
}
```

---

## 🔗 URL Structure

### Supported Formats
```
https://masspost.store              → Auto-detect language
https://masspost.store/?lang=de     → Force German
https://masspost.store/?lang=en     → Force English
https://masspost.store/page?lang=de → Works on all pages
```

### Priority Order
1. **URL parameter** (`?lang=de`) - Highest priority
2. **localStorage** (`mediamass_lang`)
3. **Browser language** (`navigator.language`)
4. **Fallback** (`de` - default)

---

## 🧩 Translation File Structure

### Main Translation File (`translations/de.json`)
```json
{
  "meta": {
    "lang": "de",
    "title": "Page Title",
    "description": "Meta description",
    "keywords": "keyword1, keyword2"
  },
  "nav": {
    "home": "Startseite",
    "features": "Features",
    "pricing": "Preise",
    "contact": "Kontakt"
  },
  "hero": {
    "title": "Headline",
    "subtitle": "Subheadline",
    "cta": "Call to Action"
  }
}
```

### Nested Keys
Use dot notation for nested objects:
```html
<h1 data-i18n="hero.title">...</h1>
<!-- Translates to translations.hero.title -->
```

---

## 🔍 SEO Features

### Automatic hreflang Tags
```html
<link rel="alternate" hreflang="de" href="https://masspost.store/?lang=de">
<link rel="alternate" hreflang="en" href="https://masspost.store/?lang=en">
<link rel="alternate" hreflang="x-default" href="https://masspost.store/?lang=de">
```

### Dynamic Meta Tags
```javascript
// In translations/de.json
{
  "meta": {
    "title": "German Title",
    "description": "German Description",
    "og_title": "Open Graph Title",
    "og_description": "Open Graph Description"
  }
}
```

These automatically update:
- `<title>`
- `<meta name="description">`
- `<meta property="og:title">`
- `<meta property="og:description">`
- `<meta property="twitter:title">`
- `<meta property="twitter:description">`

### Canonical URL
Automatically includes current language:
```html
<link rel="canonical" href="https://masspost.store/?lang=de">
```

---

## 🎯 Best Practices

### 1. Always Provide Fallback Text
```html
<!-- ✅ Good -->
<button data-i18n="cta.button">Get Started</button>

<!-- ❌ Bad -->
<button data-i18n="cta.button"></button>
```

### 2. Use Semantic Keys
```javascript
// ✅ Good
"nav.pricing" → "Preise"
"hero.cta_primary" → "Jetzt starten"

// ❌ Bad
"text1" → "Preise"
"btn2" → "Jetzt starten"
```

### 3. Keep Translations Organized
```json
{
  "nav": { /* Navigation items */ },
  "hero": { /* Hero section */ },
  "features": { /* Features section */ },
  "footer": { /* Footer content */ }
}
```

### 4. Test All Languages
```bash
# German
http://localhost:8000/?lang=de

# English
http://localhost:8000/?lang=en
```

---

## 📁 File Structure

```
masspost-website/
├── i18n.js                    # Core i18n system (13KB)
├── translations/
│   ├── de.json                # German translations (5.6KB)
│   ├── en.json                # English translations (5.3KB)
│   ├── pricing-de.json        # Optional: Page-specific
│   └── pricing-en.json
├── index.html                 # Main page with data-i18n attributes
├── preisliste.html
├── contact.html
└── other-pages.html
```

---

## 🐛 Troubleshooting

### Problem: "Translations not working"
**Solution:**
```javascript
// Check console for errors
console.log(window.i18n); // Should be defined
console.log(window.i18n.translations); // Should be object
```

### Problem: "Language switcher not visible"
**Solution:**
```javascript
// Check if i18n.js is loaded
document.querySelector('.language-switcher'); // Should not be null

// If null, check:
// 1. Is i18n.js included in <head>?
// 2. Is navigation structure correct?
```

### Problem: "Translation key not found"
**Solution:**
```javascript
// Check console for warning:
// ⚠️ Translation key not found: xyz.abc

// Fix: Add key to translations/de.json and translations/en.json
{
  "xyz": {
    "abc": "Translation text"
  }
}
```

### Problem: "Language doesn't persist"
**Solution:**
```javascript
// Check localStorage
localStorage.getItem('mediamass_lang'); // Should be 'de' or 'en'

// Clear and retry
localStorage.removeItem('mediamass_lang');
location.reload();
```

---

## 🚀 Adding More Languages

### Step 1: Add Language Code
```javascript
// In i18n.js, line ~7
this.supportedLanguages = ['de', 'en', 'fr', 'es']; // Add 'fr', 'es', etc.
```

### Step 2: Create Translation Files
```
translations/fr.json
translations/es.json
```

### Step 3: Update Language Switcher (optional)
```javascript
// In i18n.js, createLanguageSwitcher() method
// Add buttons for new languages:
<button data-lang="fr">🇫🇷 FR</button>
<button data-lang="es">🇪🇸 ES</button>
```

### Step 4: Test
```
http://localhost:8000/?lang=fr
```

---

## 🔒 Security

### XSS Protection
✅ Uses `textContent` (not `innerHTML`) by default  
✅ For HTML content, use `data-i18n-html` (sanitize translations!)

### No eval()
✅ No dynamic code execution  
✅ Pure JSON translations

### CSP Compatible
✅ No inline scripts (except Tailwind CDN)  
✅ No unsafe-eval

### localStorage
✅ Only stores language preference (`de`/`en`)  
✅ No sensitive data

---

## 📊 Performance

### Metrics
- **i18n.js:** 13KB (~4KB gzipped)
- **Translation file:** ~5KB (~2KB gzipped)
- **Initialization:** ~50ms
- **Language switch:** ~10ms
- **Memory:** < 100KB

### Optimization Tips
1. **Preload translations:**
   ```html
   <link rel="preload" href="translations/de.json" as="fetch" crossorigin>
   ```

2. **Cache translations:**
   ```javascript
   // In service worker (optional)
   cache.addAll([
     '/translations/de.json',
     '/translations/en.json'
   ]);
   ```

---

## 📝 Examples

### Example 1: Simple Page
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>My Site</title>
    <script src="i18n.js"></script>
</head>
<body>
    <nav>
        <a href="#" data-i18n="nav.home">Home</a>
        <a href="#" data-i18n="nav.about">About</a>
    </nav>
    
    <h1 data-i18n="hero.title">Welcome</h1>
    <p data-i18n="hero.text">Description</p>
    
    <button data-i18n="cta.button">Get Started</button>
</body>
</html>
```

### Example 2: Form
```html
<form>
    <input type="text" data-i18n="form.name" placeholder="Name">
    <input type="email" data-i18n="form.email" placeholder="Email">
    <textarea data-i18n="form.message" placeholder="Message"></textarea>
    <button type="submit" data-i18n="form.submit">Send</button>
</form>
```

### Example 3: Dynamic Content
```javascript
// Load product data
fetch('/api/products')
    .then(r => r.json())
    .then(products => {
        products.forEach(p => {
            const name = window.i18n.t(`products.${p.id}.name`);
            const desc = window.i18n.t(`products.${p.id}.description`);
            // Render product...
        });
    });
```

---

## 📚 API Reference

### `i18n.getCurrentLanguage()`
Returns current language code (`'de'` or `'en'`).

### `i18n.switchLanguage(lang)`
Switches to specified language and updates page.

### `i18n.t(key)`
Gets translation for key (supports nested keys like `'nav.home'`).

### `i18n.getSupportedLanguages()`
Returns array of supported languages (`['de', 'en']`).

---

## 🤝 Contributing

### Adding Translations
1. Edit `translations/de.json` and `translations/en.json`
2. Test locally
3. Commit to Git

### Reporting Issues
- Check console for errors (F12)
- Include browser and OS info
- Provide reproduction steps

---

## 📄 License

Part of MediaMass Website  
© 2026 MediaMass. All rights reserved.

---

## 📞 Support

**Questions?**
- 📧 Email: info@masspost.store
- 💬 Telegram: @MassPostSupport
- 🐛 Issues: https://github.com/Tacotitti/vidimass-website/issues

---

**Version:** 1.0.0  
**Last Updated:** 2026-04-18  
**Status:** ✅ Production Ready
