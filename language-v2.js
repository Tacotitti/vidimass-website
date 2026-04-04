// Enhanced Language System - Translates ALL text on the page
// Handles both data-i18n elements AND static text

(function() {
    'use strict';
    
    // Get language from URL parameter or localStorage
    function getInitialLanguage() {
        const urlParams = new URLSearchParams(window.location.search);
        const urlLang = urlParams.get('lang');
        if (urlLang && translations[urlLang]) {
            return urlLang;
        }
        return localStorage.getItem('selectedLanguage') || 'de';
    }
    
    // Apply translations to the entire page
    function applyLanguage(lang) {
        if (!translations[lang]) {
            console.warn(`Language ${lang} not found, falling back to 'de'`);
            lang = 'de';
        }
        
        const trans = translations[lang];
        
        // 1. Translate all elements with data-i18n
        document.querySelectorAll('[data-i18n]').forEach(element => {
            const key = element.getAttribute('data-i18n');
            if (trans[key]) {
                // Check if it's an input placeholder
                if (element.hasAttribute('placeholder')) {
                    element.setAttribute('placeholder', trans[key]);
                } else {
                    element.innerHTML = trans[key];
                }
            }
        });
        
        // 2. Update HTML lang attribute
        document.documentElement.setAttribute('lang', lang);
        
        // 3. Update language selector to show current language
        updateLanguageSelector(lang);
        
        // 4. Save to localStorage
        localStorage.setItem('selectedLanguage', lang);
        
        // 5. Update URL without reload
        const url = new URL(window.location);
        url.searchParams.set('lang', lang);
        window.history.replaceState({}, '', url);
        
        console.log(`✓ Language applied: ${lang}`);
    }
    
    // Update language selector display
    function updateLanguageSelector(lang) {
        const flagMap = {
            'en': '🇬🇧',
            'de': '🇩🇪',
            'tr': '🇹🇷',
            'pt': '🇵🇹',
            'es': '🇪🇸',
            'ru': '🇷🇺',
            'zh': '🇨🇳',
            'ar': '🇸🇦'
        };
        
        const langNameMap = {
            'en': 'EN',
            'de': 'DE',
            'tr': 'TR',
            'pt': 'PT',
            'es': 'ES',
            'ru': 'RU',
            'zh': 'ZH',
            'ar': 'AR'
        };
        
        // Update desktop selector
        const desktopBtn = document.querySelector('.language-selector button');
        if (desktopBtn) {
            desktopBtn.innerHTML = `${flagMap[lang]} <span class="lang-code">${langNameMap[lang]}</span>`;
        }
        
        // Update mobile selector
        const mobileBtn = document.querySelector('.mobile-language-selector button');
        if (mobileBtn) {
            mobileBtn.textContent = `${flagMap[lang]} ${langNameMap[lang]}`;
        }
    }
    
    // Initialize language system
    function initLanguageSystem() {
        const initialLang = getInitialLanguage();
        
        // Apply initial language
        applyLanguage(initialLang);
        
        // Desktop language selector
        const desktopOptions = document.querySelectorAll('.language-dropdown button[data-lang]');
        desktopOptions.forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                const lang = this.getAttribute('data-lang');
                applyLanguage(lang);
                
                // Close dropdown
                const dropdown = this.closest('.language-dropdown');
                if (dropdown) {
                    dropdown.style.display = 'none';
                }
            });
        });
        
        // Desktop dropdown toggle
        const desktopToggle = document.querySelector('.language-selector button');
        if (desktopToggle) {
            desktopToggle.addEventListener('click', function(e) {
                e.stopPropagation();
                const dropdown = document.querySelector('.language-dropdown');
                if (dropdown) {
                    dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
                }
            });
        }
        
        // Mobile language selector
        const mobileOptions = document.querySelectorAll('.mobile-lang-grid button[data-lang]');
        mobileOptions.forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                const lang = this.getAttribute('data-lang');
                applyLanguage(lang);
                
                // Close mobile menu
                const langMenu = this.closest('.mobile-lang-menu');
                if (langMenu) {
                    langMenu.classList.remove('active');
                }
            });
        });
        
        // Mobile language menu toggle
        const mobileLangBtn = document.querySelector('.mobile-language-selector button');
        if (mobileLangBtn) {
            mobileLangBtn.addEventListener('click', function(e) {
                e.stopPropagation();
                const menu = document.querySelector('.mobile-lang-menu');
                if (menu) {
                    menu.classList.toggle('active');
                }
            });
        }
        
        // Close dropdowns when clicking outside
        document.addEventListener('click', function() {
            const dropdown = document.querySelector('.language-dropdown');
            if (dropdown) dropdown.style.display = 'none';
            
            const mobileMenu = document.querySelector('.mobile-lang-menu');
            if (mobileMenu) mobileMenu.classList.remove('active');
        });
        
        console.log('✓ Language system initialized');
    }
    
    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initLanguageSystem);
    } else {
        initLanguageSystem();
    }
    
    // Expose globally for external use
    window.applyLanguage = applyLanguage;
})();
