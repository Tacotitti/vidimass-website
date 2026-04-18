/**
 * i18n.js - Internationalization System for MediaMass
 * Supports: DE (Deutsch), EN (English)
 * Features: URL parameters, localStorage, auto-detection, SEO optimization
 */

class I18n {
    constructor() {
        this.currentLang = 'de'; // Default language
        this.translations = {};
        this.supportedLanguages = ['de', 'en'];
        this.fallbackLang = 'de';
        
        // Initialize
        this.init();
    }

    /**
     * Initialize i18n system
     */
    async init() {
        // 1. Detect language from URL, localStorage, or browser
        this.currentLang = this.detectLanguage();
        
        // 2. Load translations
        await this.loadTranslations(this.currentLang);
        
        // 3. Apply translations to page
        this.translatePage();
        
        // 4. Update HTML lang attribute
        document.documentElement.setAttribute('lang', this.currentLang);
        
        // 5. Update hreflang tags
        this.updateHreflangTags();
        
        // 6. Setup language switcher
        this.setupLanguageSwitcher();
        
        // 7. Save preference
        this.saveLanguagePreference(this.currentLang);
    }

    /**
     * Detect language from multiple sources (priority order)
     * 1. URL parameter (?lang=de or ?lang=en)
     * 2. localStorage
     * 3. Browser language
     * 4. Fallback to default (de)
     */
    detectLanguage() {
        // 1. Check URL parameter
        const urlParams = new URLSearchParams(window.location.search);
        const urlLang = urlParams.get('lang');
        if (urlLang && this.supportedLanguages.includes(urlLang)) {
            return urlLang;
        }

        // 2. Check localStorage
        const storedLang = localStorage.getItem('mediamass_lang');
        if (storedLang && this.supportedLanguages.includes(storedLang)) {
            return storedLang;
        }

        // 3. Check browser language
        const browserLang = navigator.language || navigator.userLanguage;
        const browserLangCode = browserLang.split('-')[0].toLowerCase();
        if (this.supportedLanguages.includes(browserLangCode)) {
            return browserLangCode;
        }

        // 4. Fallback
        return this.fallbackLang;
    }

    /**
     * Load translation JSON file
     */
    async loadTranslations(lang) {
        try {
            const response = await fetch(`translations/${lang}.json`);
            if (!response.ok) {
                throw new Error(`Failed to load ${lang}.json`);
            }
            this.translations = await response.json();
            return true;
        } catch (error) {
            console.error('Translation loading error:', error);
            
            // Try fallback language
            if (lang !== this.fallbackLang) {
                console.warn(`Falling back to ${this.fallbackLang}`);
                const fallbackResponse = await fetch(`translations/${this.fallbackLang}.json`);
                this.translations = await fallbackResponse.json();
                this.currentLang = this.fallbackLang;
            }
            return false;
        }
    }

    /**
     * Get translation by key (supports nested keys like "hero.headline_part1")
     */
    t(key) {
        const keys = key.split('.');
        let value = this.translations;

        for (const k of keys) {
            if (value && typeof value === 'object' && k in value) {
                value = value[k];
            } else {
                console.warn(`Translation key not found: ${key}`);
                return key; // Return key if translation not found
            }
        }

        return value;
    }

    /**
     * Translate entire page using data-i18n attributes
     */
    translatePage() {
        // Translate meta tags
        this.updateMetaTags();

        // Translate elements with data-i18n attribute
        document.querySelectorAll('[data-i18n]').forEach(element => {
            const key = element.getAttribute('data-i18n');
            const translation = this.t(key);
            
            // Check if it's an input placeholder
            if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
                element.placeholder = translation;
            } else {
                element.textContent = translation;
            }
        });

        // Translate elements with data-i18n-html (for HTML content)
        document.querySelectorAll('[data-i18n-html]').forEach(element => {
            const key = element.getAttribute('data-i18n-html');
            const translation = this.t(key);
            element.innerHTML = translation;
        });

        // Translate aria-labels
        document.querySelectorAll('[data-i18n-aria]').forEach(element => {
            const key = element.getAttribute('data-i18n-aria');
            const translation = this.t(key);
            element.setAttribute('aria-label', translation);
        });

        // Translate titles
        document.querySelectorAll('[data-i18n-title]').forEach(element => {
            const key = element.getAttribute('data-i18n-title');
            const translation = this.t(key);
            element.setAttribute('title', translation);
        });
    }

    /**
     * Update meta tags for SEO
     */
    updateMetaTags() {
        // Update title
        const title = this.t('meta.title');
        if (title) {
            document.title = title;
        }

        // Update meta description
        const description = this.t('meta.description');
        if (description) {
            this.updateMetaTag('name', 'description', description);
        }

        // Update meta keywords
        const keywords = this.t('meta.keywords');
        if (keywords) {
            this.updateMetaTag('name', 'keywords', keywords);
        }

        // Update Open Graph tags
        const ogTitle = this.t('meta.og_title');
        if (ogTitle) {
            this.updateMetaTag('property', 'og:title', ogTitle);
        }

        const ogDescription = this.t('meta.og_description');
        if (ogDescription) {
            this.updateMetaTag('property', 'og:description', ogDescription);
        }

        // Update Twitter tags
        if (ogTitle) {
            this.updateMetaTag('property', 'twitter:title', ogTitle);
        }
        if (ogDescription) {
            this.updateMetaTag('property', 'twitter:description', ogDescription);
        }
    }

    /**
     * Helper to update or create meta tag
     */
    updateMetaTag(attribute, attributeValue, content) {
        let element = document.querySelector(`meta[${attribute}="${attributeValue}"]`);
        if (!element) {
            element = document.createElement('meta');
            element.setAttribute(attribute, attributeValue);
            document.head.appendChild(element);
        }
        element.setAttribute('content', content);
    }

    /**
     * Update hreflang tags for SEO
     */
    updateHreflangTags() {
        // Remove existing hreflang tags
        document.querySelectorAll('link[rel="alternate"]').forEach(link => {
            if (link.getAttribute('hreflang')) {
                link.remove();
            }
        });

        // Get current URL without query parameters
        const baseUrl = window.location.origin + window.location.pathname;

        // Add hreflang tags for all supported languages
        this.supportedLanguages.forEach(lang => {
            const link = document.createElement('link');
            link.rel = 'alternate';
            link.hreflang = lang;
            link.href = `${baseUrl}?lang=${lang}`;
            document.head.appendChild(link);
        });

        // Add x-default hreflang
        const defaultLink = document.createElement('link');
        defaultLink.rel = 'alternate';
        defaultLink.hreflang = 'x-default';
        defaultLink.href = `${baseUrl}?lang=${this.fallbackLang}`;
        document.head.appendChild(defaultLink);

        // Update canonical URL to include current language
        let canonical = document.querySelector('link[rel="canonical"]');
        if (!canonical) {
            canonical = document.createElement('link');
            canonical.rel = 'canonical';
            document.head.appendChild(canonical);
        }
        canonical.href = `${baseUrl}?lang=${this.currentLang}`;
    }

    /**
     * Save language preference to localStorage
     */
    saveLanguagePreference(lang) {
        localStorage.setItem('mediamass_lang', lang);
    }

    /**
     * Switch language
     */
    async switchLanguage(lang) {
        if (!this.supportedLanguages.includes(lang)) {
            console.error(`Language ${lang} not supported`);
            return;
        }

        // Load new translations
        await this.loadTranslations(lang);

        // Update current language
        this.currentLang = lang;

        // Translate page
        this.translatePage();

        // Update HTML lang attribute
        document.documentElement.setAttribute('lang', lang);

        // Update hreflang tags
        this.updateHreflangTags();

        // Save preference
        this.saveLanguagePreference(lang);

        // Update URL without reload
        const url = new URL(window.location);
        url.searchParams.set('lang', lang);
        window.history.pushState({}, '', url);

        // Update language switcher UI
        this.updateLanguageSwitcherUI();

        // Dispatch event for other components
        window.dispatchEvent(new CustomEvent('languageChanged', { detail: { lang } }));
    }

    /**
     * Setup language switcher UI component
     */
    setupLanguageSwitcher() {
        // Create language switcher if it doesn't exist
        if (!document.querySelector('.language-switcher')) {
            this.createLanguageSwitcher();
        }

        // Add click handlers to language switcher buttons
        document.querySelectorAll('.lang-switch-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const lang = btn.getAttribute('data-lang');
                this.switchLanguage(lang);
            });
        });

        // Update UI to show current language
        this.updateLanguageSwitcherUI();
    }

    /**
     * Create language switcher component in navigation
     */
    createLanguageSwitcher() {
        const nav = document.querySelector('nav .container .flex');
        if (!nav) return;

        // Create switcher for desktop
        const desktopNav = nav.querySelector('.hidden.md\\:flex');
        if (desktopNav) {
            const switcherHTML = `
                <div class="language-switcher flex items-center gap-2 ml-4">
                    <button class="lang-switch-btn px-3 py-1.5 rounded-lg transition-all duration-200 text-sm font-medium" data-lang="de">
                        DE
                    </button>
                    <span class="text-gray-500">|</span>
                    <button class="lang-switch-btn px-3 py-1.5 rounded-lg transition-all duration-200 text-sm font-medium" data-lang="en">
                        EN
                    </button>
                </div>
            `;
            desktopNav.insertAdjacentHTML('beforeend', switcherHTML);
        }

        // Create switcher for mobile menu
        const mobileMenu = document.querySelector('.mobile-menu');
        if (mobileMenu) {
            const mobileSwitcherHTML = `
                <div class="language-switcher-mobile flex items-center justify-center gap-4 mt-6 pt-6 border-t border-white/10">
                    <button class="lang-switch-btn px-4 py-2 rounded-lg transition-all duration-200 font-medium" data-lang="de">
                        🇩🇪 Deutsch
                    </button>
                    <button class="lang-switch-btn px-4 py-2 rounded-lg transition-all duration-200 font-medium" data-lang="en">
                        🇬🇧 English
                    </button>
                </div>
            `;
            mobileMenu.insertAdjacentHTML('beforeend', mobileSwitcherHTML);
        }
    }

    /**
     * Update language switcher UI to show active language
     */
    updateLanguageSwitcherUI() {
        document.querySelectorAll('.lang-switch-btn').forEach(btn => {
            const lang = btn.getAttribute('data-lang');
            if (lang === this.currentLang) {
                btn.classList.add('bg-gradient-to-r', 'from-violet-600', 'to-pink-600', 'text-white');
                btn.classList.remove('text-gray-400', 'hover:text-white');
            } else {
                btn.classList.remove('bg-gradient-to-r', 'from-violet-600', 'to-pink-600', 'text-white');
                btn.classList.add('text-gray-400', 'hover:text-white');
            }
        });
    }

    /**
     * Get current language
     */
    getCurrentLanguage() {
        return this.currentLang;
    }

    /**
     * Get all supported languages
     */
    getSupportedLanguages() {
        return this.supportedLanguages;
    }
}

// Initialize i18n system when DOM is ready
let i18nInstance = null;

document.addEventListener('DOMContentLoaded', async () => {
    i18nInstance = new I18n();
    
    // Make i18n globally accessible
    window.i18n = i18nInstance;
    
    console.log('✅ i18n system initialized. Current language:', i18nInstance.getCurrentLanguage());
});

// Global helper function for onclick handlers
function switchLanguage(lang) {
    if (window.i18n) {
        window.i18n.switchLanguage(lang);
    }
}

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = I18n;
}
