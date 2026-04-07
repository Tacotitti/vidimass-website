// Enhanced Language System - Translates ALL text on the page
// Handles both data-i18n elements AND static text

(function() {
    'use strict';
    
    // Get language from URL parameter or localStorage
    function getInitialLanguage() {
        const urlParams = new URLSearchParams(window.location.search);
        const urlLang = urlParams.get('lang');
        // Check if URL lang is valid (safely check if translations exists)
        if (urlLang && typeof translations !== 'undefined' && translations[urlLang]) {
            localStorage.setItem('selectedLanguage', urlLang); // Save URL lang
            return urlLang;
        }
        // Return saved language or default
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
                element.textContent = trans[key];
            }
        });
        
        // 1b. Translate elements with data-i18n-html (preserves HTML)
        document.querySelectorAll('[data-i18n-html]').forEach(element => {
            const key = element.getAttribute('data-i18n-html');
            if (trans[key]) {
                element.innerHTML = trans[key];
            }
        });
        
        // 1c. Translate placeholders with data-i18n-placeholder
        document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
            const key = element.getAttribute('data-i18n-placeholder');
            if (trans[key]) {
                element.setAttribute('placeholder', trans[key]);
            }
        });
        
        // 1d. Translate optgroup labels with data-i18n-label
        document.querySelectorAll('[data-i18n-label]').forEach(element => {
            const key = element.getAttribute('data-i18n-label');
            if (trans[key]) {
                element.setAttribute('label', trans[key]);
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
        const langNameMap = {
            'en': 'English',
            'de': 'Deutsch',
            'tr': 'Türkçe',
            'pt': 'Português',
            'es': 'Español',
            'ru': 'Русский',
            'zh': '中文',
            'ar': 'العربية'
        };
        
        // Update desktop selector button (NO FLAGS, just text)
        const desktopBtn = document.getElementById('lang-button');
        if (desktopBtn) {
            const nameSpan = desktopBtn.querySelector('.lang-name');
            if (nameSpan) {
                nameSpan.textContent = langNameMap[lang];
            }
            // Hide flag span
            const flagSpan = desktopBtn.querySelector('.flag');
            if (flagSpan) flagSpan.style.display = 'none';
        }
        
        // Update active state in dropdown
        document.querySelectorAll('.lang-option').forEach(opt => {
            opt.classList.remove('active');
            if (opt.getAttribute('data-lang') === lang) {
                opt.classList.add('active');
            }
            // Hide flags in dropdown too
            const flag = opt.querySelector('.flag');
            if (flag) flag.style.display = 'none';
        });
        
        // Update mobile selector (NO FLAGS)
        const mobileBtn = document.querySelector('.mobile-language-selector button');
        if (mobileBtn) {
            mobileBtn.textContent = langNameMap[lang];
        }
    }
    
    // Initialize language system
    function initLanguageSystem() {
        const initialLang = getInitialLanguage();
        
        // Apply initial language
        applyLanguage(initialLang);
        
        // Desktop language selector
        const desktopOptions = document.querySelectorAll('.lang-dropdown button[data-lang]');
        desktopOptions.forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                const lang = this.getAttribute('data-lang');
                applyLanguage(lang);
                
                // Close dropdown
                const dropdown = document.getElementById('lang-dropdown');
                if (dropdown) {
                    dropdown.classList.remove('active');
                }
            });
        });
        
        // Desktop dropdown toggle
        const desktopToggle = document.getElementById('lang-button');
        if (desktopToggle) {
            desktopToggle.addEventListener('click', function(e) {
                e.stopPropagation();
                const dropdown = document.getElementById('lang-dropdown');
                if (dropdown) {
                    dropdown.classList.toggle('active');
                }
            });
        }
        
        // Mobile language selector (FIXED - targets .mobile-lang-btn)
        function attachMobileLangListeners() {
            const mobileOptions = document.querySelectorAll('.mobile-lang-btn[data-lang]');
            mobileOptions.forEach(btn => {
                btn.addEventListener('click', function(e) {
                    e.preventDefault();
                    const lang = this.getAttribute('data-lang');
                    applyLanguage(lang);
                    
                    // Update active state in mobile selector
                    document.querySelectorAll('.mobile-lang-btn').forEach(opt => {
                        opt.classList.remove('active');
                    });
                    this.classList.add('active');
                    
                    // Close mobile menu
                    const mobileMenu = document.querySelector('.mobile-menu');
                    const overlay = document.querySelector('.mobile-overlay');
                    if (mobileMenu) mobileMenu.classList.remove('active');
                    if (overlay) overlay.classList.remove('active');
                });
            });
        }
        
        // Attach mobile listeners immediately
        attachMobileLangListeners();
        
        // Re-attach after script.js creates mobile menu (delay for DOM update)
        setTimeout(attachMobileLangListeners, 100);
        
        // Close dropdowns when clicking outside
        document.addEventListener('click', function() {
            const dropdown = document.getElementById('lang-dropdown');
            if (dropdown) dropdown.classList.remove('active');
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
