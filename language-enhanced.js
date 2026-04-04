// Enhanced language system - translates ALL visible text automatically
// Extends the existing language.js to handle elements without data-i18n

document.addEventListener('DOMContentLoaded', function() {
    
    // Auto-translate all text nodes when language changes
    function translateAllText(lang) {
        const translations = window.translations[lang];
        if (!translations) return;
        
        // 1. Translate elements with data-i18n (existing)
        document.querySelectorAll('[data-i18n]').forEach(element => {
            const key = element.getAttribute('data-i18n');
            if (translations[key]) {
                element.textContent = translations[key];
            }
        });
        
        // 2. NEW: Translate navigation links
        translateElement('a[href="index.html#features"]', translations.nav_features || 'Features');
        translateElement('a[href="social-media-charting.html"]', translations.nav_charting || 'Social Media Charting');
        translateElement('a[href="preisliste.html"]', translations.nav_pricing || 'Preisliste');
        translateElement('a[href="contact.html"]:not([data-i18n])', translations.nav_contact || 'Kontakt');
        
        // 3. NEW: Translate page titles
        if (translations.page_title) {
            document.title = translations.page_title;
        }
        
        // 4. NEW: Translate static headings
        translateByText('h1, h2, h3', {
            'Mass Posting': translations.hero_title_1 || 'Mass Posting',
            'MASS POSTING': translations.hero_title_1 || 'MASS POSTING',
            'Charting für Labels und Künstler weltweit': translations.features_heading || 'Charting für Labels und Künstler weltweit',
            'Transparente Preise für TikTok und Instagram Mass Posting': translations.pricing_heading || 'Transparente Preise für TikTok und Instagram Mass Posting',
            'Kontaktieren Sie uns': translations.contact_heading || 'Kontaktieren Sie uns',
        });
        
        // 5. NEW: Translate form labels
        translateElement('label[for="name"]', translations.contact_name_label || 'Name');
        translateElement('label[for="email"]', translations.contact_email_label || 'E-Mail');
        translateElement('label[for="category"]', translations.contact_category_label || 'Kategorie');
        translateElement('label[for="package"]', translations.contact_package_label || 'Gewünschtes Paket');
        translateElement('label[for="message"]', translations.contact_message_label || 'Nachricht');
        
        // 6. NEW: Translate placeholders
        translatePlaceholder('input[name="name"]', translations.contact_name_placeholder || 'Ihr vollständiger Name');
        translatePlaceholder('input[name="email"]', translations.contact_email_placeholder || 'ihre.email@beispiel.de');
        translatePlaceholder('textarea[name="message"]', translations.contact_message_placeholder || 'Beschreiben Sie Ihre Anfrage...');
        
        // 7. NEW: Translate buttons
        translateElement('button[type="submit"]', translations.contact_submit || 'Nachricht senden');
        
        // 8. NEW: Translate footer
        document.querySelectorAll('footer a').forEach(link => {
            const href = link.getAttribute('href');
            if (href === 'datenschutz.html') link.textContent = translations.footer_privacy || 'Datenschutz';
            if (href === 'nutzungsbedingungen.html') link.textContent = translations.footer_terms || 'Nutzungsbedingungen';
            if (href === 'contact.html' && link.closest('footer')) link.textContent = translations.footer_contact || 'Kontakt';
        });
        
        // 9. Update lang attribute
        document.documentElement.lang = lang;
    }
    
    function translateElement(selector, text) {
        const el = document.querySelector(selector);
        if (el) el.textContent = text;
    }
    
    function translatePlaceholder(selector, text) {
        const el = document.querySelector(selector);
        if (el) el.placeholder = text;
    }
    
    function translateByText(selector, mappings) {
        document.querySelectorAll(selector).forEach(el => {
            const original = el.textContent.trim();
            if (mappings[original]) {
                el.textContent = mappings[original];
            }
        });
    }
    
    // Override existing applyLanguage to use enhanced version
    window.applyLanguageEnhanced = translateAllText;
    
    // Re-apply on language change
    const originalApplyLanguage = window.applyLanguage;
    if (originalApplyLanguage) {
        window.applyLanguage = function(lang) {
            originalApplyLanguage(lang);
            translateAllText(lang);
        };
    }
});
