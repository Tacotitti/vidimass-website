// Pre-load language setting to avoid flash of default language
// This script runs BEFORE translations.js and language.js
(function() {
    'use strict';
    
    // Get saved language immediately
    const savedLang = localStorage.getItem('selectedLanguage');
    
    // Set HTML lang attribute immediately (before page renders)
    if (savedLang) {
        document.documentElement.setAttribute('lang', savedLang);
        console.log('✓ Pre-loaded language:', savedLang);
    }
    
    // If URL has lang parameter, use it and save it
    const urlParams = new URLSearchParams(window.location.search);
    const urlLang = urlParams.get('lang');
    if (urlLang) {
        localStorage.setItem('selectedLanguage', urlLang);
        document.documentElement.setAttribute('lang', urlLang);
        console.log('✓ URL language detected and saved:', urlLang);
    }
})();
