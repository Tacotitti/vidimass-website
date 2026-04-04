// MediaMass - Language Switcher System

// Language configuration
const SUPPORTED_LANGUAGES = {
    en: { name: 'English', flag: '🇬🇧' },
    de: { name: 'Deutsch', flag: '🇩🇪' },
    tr: { name: 'Türkçe', flag: '🇹🇷' },
    pt: { name: 'Português', flag: '🇵🇹' },
    es: { name: 'Español', flag: '🇪🇸' },
    ru: { name: 'Русский', flag: '🇷🇺' },
    zh: { name: '中文', flag: '🇨🇳' },
    ar: { name: 'العربية', flag: '🇸🇦' }
};

let currentLanguage = 'en';

// Get user's browser language or saved preference
function detectLanguage() {
    // Check localStorage first
    const savedLang = localStorage.getItem('mediamass_language');
    if (savedLang && SUPPORTED_LANGUAGES[savedLang]) {
        return savedLang;
    }
    
    // Detect browser language
    const browserLang = navigator.language || navigator.userLanguage;
    const langCode = browserLang.split('-')[0].toLowerCase();
    
    // Return detected language if supported, otherwise default to English
    return SUPPORTED_LANGUAGES[langCode] ? langCode : 'en';
}

// Change language
function changeLanguage(lang) {
    if (!SUPPORTED_LANGUAGES[lang]) {
        console.error('Language not supported:', lang);
        return;
    }
    
    currentLanguage = lang;
    localStorage.setItem('mediamass_language', lang);
    
    // Update all translatable elements
    updatePageContent();
    
    // Update language selector display
    updateLanguageSelector();
    
    // Update HTML lang attribute
    document.documentElement.lang = lang;
    
    // Apply RTL for Arabic
    if (lang === 'ar') {
        document.documentElement.dir = 'rtl';
        document.body.classList.add('rtl');
    } else {
        document.documentElement.dir = 'ltr';
        document.body.classList.remove('rtl');
    }
}

// Update all page content with translations
function updatePageContent() {
    const trans = translations[currentLanguage];
    
    // Navigation
    setText('[data-i18n="nav_features"]', trans.nav_features);
    setText('[data-i18n="nav_stats"]', trans.nav_stats);
    setText('[data-i18n="nav_packages"]', trans.nav_packages);
    setText('[data-i18n="nav_get_started"]', trans.nav_get_started);
    
    // Hero Section
    setText('[data-i18n="hero_badge"]', trans.hero_badge);
    setHTML('[data-i18n="hero_title_1"]', trans.hero_title_1);
    setHTML('[data-i18n="hero_title_2"]', trans.hero_title_2);
    setHTML('[data-i18n="hero_subtitle"]', trans.hero_subtitle);
    setText('[data-i18n="hero_cta_primary"]', trans.hero_cta_primary);
    setText('[data-i18n="hero_cta_secondary"]', trans.hero_cta_secondary);
    setText('[data-i18n="hero_trust_1"]', trans.hero_trust_1);
    setText('[data-i18n="hero_trust_2"]', trans.hero_trust_2);
    setText('[data-i18n="hero_trust_3"]', trans.hero_trust_3);
    
    // Stats Section
    setText('[data-i18n="stats_videos_count"]', trans.stats_videos_count);
    setText('[data-i18n="stats_videos_label"]', trans.stats_videos_label);
    setText('[data-i18n="stats_videos_desc"]', trans.stats_videos_desc);
    setText('[data-i18n="stats_platforms_count"]', trans.stats_platforms_count);
    setText('[data-i18n="stats_platforms_label"]', trans.stats_platforms_label);
    setText('[data-i18n="stats_platforms_desc"]', trans.stats_platforms_desc);
    setText('[data-i18n="stats_distribution_count"]', trans.stats_distribution_count);
    setText('[data-i18n="stats_distribution_label"]', trans.stats_distribution_label);
    setText('[data-i18n="stats_distribution_desc"]', trans.stats_distribution_desc);
    
    // Features Section
    setHTML('[data-i18n="features_title_1"]', trans.features_title_1);
    setHTML('[data-i18n="features_title_2"]', trans.features_title_2);
    setText('[data-i18n="features_subtitle"]', trans.features_subtitle);
    
    for (let i = 1; i <= 6; i++) {
        setText(`[data-i18n="feature_${i}_title"]`, trans[`feature_${i}_title`]);
        setText(`[data-i18n="feature_${i}_desc"]`, trans[`feature_${i}_desc`]);
    }
    
    // Packages Section
    setHTML('[data-i18n="packages_title_1"]', trans.packages_title_1);
    setHTML('[data-i18n="packages_title_2"]', trans.packages_title_2);
    setText('[data-i18n="packages_subtitle"]', trans.packages_subtitle);
    
    // Starter Package
    setText('[data-i18n="package_starter_name"]', trans.package_starter_name);
    setText('[data-i18n="package_starter_price"]', trans.package_starter_price);
    setText('[data-i18n="package_starter_period"]', trans.package_starter_period);
    setText('[data-i18n="package_starter_desc"]', trans.package_starter_desc);
    for (let i = 1; i <= 4; i++) {
        setText(`[data-i18n="package_starter_feature_${i}"]`, trans[`package_starter_feature_${i}`]);
    }
    setText('[data-i18n="package_starter_cta"]', trans.package_starter_cta);
    
    // Pro Package
    setText('[data-i18n="package_pro_name"]', trans.package_pro_name);
    setText('[data-i18n="package_pro_badge"]', trans.package_pro_badge);
    setText('[data-i18n="package_pro_price"]', trans.package_pro_price);
    setText('[data-i18n="package_pro_period"]', trans.package_pro_period);
    setText('[data-i18n="package_pro_desc"]', trans.package_pro_desc);
    for (let i = 1; i <= 5; i++) {
        setText(`[data-i18n="package_pro_feature_${i}"]`, trans[`package_pro_feature_${i}`]);
    }
    setText('[data-i18n="package_pro_cta"]', trans.package_pro_cta);
    
    // Enterprise Package
    setText('[data-i18n="package_enterprise_name"]', trans.package_enterprise_name);
    setText('[data-i18n="package_enterprise_price"]', trans.package_enterprise_price);
    setText('[data-i18n="package_enterprise_desc"]', trans.package_enterprise_desc);
    for (let i = 1; i <= 5; i++) {
        setText(`[data-i18n="package_enterprise_feature_${i}"]`, trans[`package_enterprise_feature_${i}`]);
    }
    setText('[data-i18n="package_enterprise_cta"]', trans.package_enterprise_cta);
    
    // Footer
    setText('[data-i18n="footer_privacy"]', trans.footer_privacy);
    setText('[data-i18n="footer_terms"]', trans.footer_terms);
    setText('[data-i18n="footer_contact"]', trans.footer_contact);
    setText('[data-i18n="footer_copyright"]', trans.footer_copyright);
}

// Helper function to set text content
function setText(selector, text) {
    const elements = document.querySelectorAll(selector);
    elements.forEach(el => {
        el.textContent = text;
    });
}

// Helper function to set HTML content
function setHTML(selector, html) {
    const elements = document.querySelectorAll(selector);
    elements.forEach(el => {
        el.innerHTML = html;
    });
}

// Create language selector dropdown
function createLanguageSelector() {
    // Check if language selector already exists in HTML
    const existingSelector = document.querySelector('.language-selector');
    if (existingSelector) {
        console.log('Language selector already in HTML, attaching events...');
        attachLanguageSelectorEvents();
        return;
    }
    
    // If not, create it dynamically (fallback)
    const nav = document.querySelector('nav .container > div');
    if (!nav) return;
    
    const langSelector = document.createElement('div');
    langSelector.className = 'language-selector';
    langSelector.innerHTML = `
        <button class="lang-current" id="lang-button">
            <span class="flag">${SUPPORTED_LANGUAGES[currentLanguage].flag}</span>
            <span class="lang-name">${SUPPORTED_LANGUAGES[currentLanguage].name}</span>
            <svg class="chevron" width="14" height="14" viewBox="0 0 14 14" fill="none">
                <path d="M3 5L7 9L11 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        </button>
        <div class="lang-dropdown" id="lang-dropdown">
            ${Object.entries(SUPPORTED_LANGUAGES).map(([code, info]) => `
                <button class="lang-option ${code === currentLanguage ? 'active' : ''}" data-lang="${code}">
                    <span class="flag">${info.flag}</span>
                    <span class="name">${info.name}</span>
                    ${code === currentLanguage ? '<span class="checkmark">✓</span>' : ''}
                </button>
            `).join('')}
        </div>
    `;
    
    // Insert before CTA button (rightmost position)
    const desktopNav = nav.querySelector('.hidden.md\\:flex');
    if (desktopNav) {
        const ctaButton = desktopNav.querySelector('.cta-button');
        if (ctaButton) {
            desktopNav.insertBefore(langSelector, ctaButton);
        } else {
            desktopNav.appendChild(langSelector);
        }
    }
    
    attachLanguageSelectorEvents();
    
    // Also create mobile version - with retry for dynamically created menu
    createMobileLanguageSelector();
}

// Create mobile language selector (separate function with retry)
function createMobileLanguageSelector() {
    // Check if mobile language buttons already exist in HTML
    const existingMobileBtns = document.querySelectorAll('.mobile-lang-btn');
    
    if (existingMobileBtns.length > 0) {
        console.log('✅ Mobile language buttons found in HTML, attaching events...');
        
        // Add click handlers for existing buttons
        existingMobileBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const lang = btn.dataset.lang;
                changeLanguage(lang);
                // Close mobile menu
                document.querySelector('.mobile-menu')?.classList.remove('active');
                document.querySelector('.mobile-overlay')?.classList.remove('active');
            });
        });
        
        return; // Exit early, buttons already exist
    }
    
    // Otherwise, try to find the container and create buttons dynamically
    const mobileLangContainer = document.getElementById('mobile-lang-selector');
    
    if (mobileLangContainer && !mobileLangContainer.querySelector('.mobile-lang-grid')) {
        const mobileLangSelector = document.createElement('div');
        mobileLangSelector.className = 'mobile-lang-grid';
        mobileLangSelector.innerHTML = `
            <div class="mobile-lang-title">🌍 Language / Sprache</div>
            ${Object.entries(SUPPORTED_LANGUAGES).map(([code, info]) => `
                <button class="mobile-lang-btn ${code === currentLanguage ? 'active' : ''}" data-lang="${code}">
                    <span class="flag">${info.flag}</span>
                    <span class="name">${info.name}</span>
                </button>
            `).join('')}
        `;
        mobileLangContainer.appendChild(mobileLangSelector);
        
        // Add click handlers for mobile
        mobileLangSelector.querySelectorAll('.mobile-lang-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const lang = btn.dataset.lang;
                changeLanguage(lang);
                // Close mobile menu
                document.querySelector('.mobile-menu')?.classList.remove('active');
                document.querySelector('.mobile-overlay')?.classList.remove('active');
            });
        });
        
        console.log('✅ Mobile language selector created dynamically!');
    } else if (!mobileLangContainer && !existingMobileBtns.length) {
        // Retry after mobile menu is created
        console.log('⏳ Mobile menu not ready yet, retrying in 100ms...');
        setTimeout(createMobileLanguageSelector, 100);
    }
}

// Attach event listeners to language selector
function attachLanguageSelectorEvents() {
    const langButton = document.getElementById('lang-button');
    const langDropdown = document.getElementById('lang-dropdown');
    
    if (!langButton || !langDropdown) {
        console.error('Language selector elements not found');
        return;
    }
    
    langButton.addEventListener('click', (e) => {
        e.stopPropagation();
        langDropdown.classList.toggle('active');
    });
    
    // Close dropdown when clicking outside
    document.addEventListener('click', () => {
        langDropdown.classList.remove('active');
    });
    
    // Language option click handlers
    document.querySelectorAll('.lang-option').forEach(option => {
        option.addEventListener('click', (e) => {
            e.stopPropagation();
            const lang = option.dataset.lang;
            changeLanguage(lang);
            langDropdown.classList.remove('active');
        });
    });
}

// Update language selector display
function updateLanguageSelector() {
    const currentButton = document.getElementById('lang-button');
    if (currentButton) {
        currentButton.innerHTML = `
            <span class="flag">${SUPPORTED_LANGUAGES[currentLanguage].flag}</span>
            <span class="lang-name">${SUPPORTED_LANGUAGES[currentLanguage].name}</span>
            <svg class="chevron" width="14" height="14" viewBox="0 0 14 14" fill="none">
                <path d="M3 5L7 9L11 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        `;
    }
    
    // Update active state
    document.querySelectorAll('.lang-option').forEach(option => {
        const lang = option.dataset.lang;
        if (lang === currentLanguage) {
            option.classList.add('active');
            option.innerHTML = `
                <span class="flag">${SUPPORTED_LANGUAGES[lang].flag}</span>
                <span class="name">${SUPPORTED_LANGUAGES[lang].name}</span>
                <span class="checkmark">✓</span>
            `;
        } else {
            option.classList.remove('active');
            option.innerHTML = `
                <span class="flag">${SUPPORTED_LANGUAGES[lang].flag}</span>
                <span class="name">${SUPPORTED_LANGUAGES[lang].name}</span>
            `;
        }
    });
}

// Initialize language system
document.addEventListener('DOMContentLoaded', function() {
    // Detect and set initial language
    currentLanguage = detectLanguage();
    
    // Create language selector
    createLanguageSelector();
    
    // Apply initial translations
    changeLanguage(currentLanguage);
    
    console.log('🌍 Language system initialized:', currentLanguage);
});
