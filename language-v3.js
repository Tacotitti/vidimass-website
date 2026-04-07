/**
 * MediaMass Language System V3
 * Completely rebuilt for reliability and robustness
 * Author: AI Agent
 * Date: 2026-04-07
 * 
 * Features:
 * - Synchronous translation loading
 * - Comprehensive error logging
 * - Fallback system (TR → DE → EN → key)
 * - Debug mode for troubleshooting
 * - Immediate translation without delays
 */

// ============================================
// 1. CONFIGURATION
// ============================================
const LANG_CONFIG = {
    defaultLang: 'de',
    supportedLangs: ['de', 'en', 'tr', 'pt', 'es'],
    storageKey: 'selectedLanguage',
    debugMode: true, // Set to false in production
    fallbackChain: ['tr', 'de', 'en'] // If key missing in TR, try DE, then EN
};

// ============================================
// 2. LOGGING UTILITY
// ============================================
function logDebug(message, data = null) {
    if (!LANG_CONFIG.debugMode) return;
    
    const timestamp = new Date().toISOString();
    const logMessage = `[Language v3 ${timestamp}] ${message}`;
    
    if (data) {
        console.log(logMessage, data);
    } else {
        console.log(logMessage);
    }
}

function logError(message, error = null) {
    const timestamp = new Date().toISOString();
    console.error(`[Language v3 ERROR ${timestamp}] ${message}`, error || '');
}

// ============================================
// 3. LANGUAGE DETECTION & PERSISTENCE
// ============================================
function detectLanguage() {
    // 1. Check URL parameter (?lang=tr)
    const urlParams = new URLSearchParams(window.location.search);
    const urlLang = urlParams.get('lang');
    if (urlLang && LANG_CONFIG.supportedLangs.includes(urlLang)) {
        logDebug(`Language from URL: ${urlLang}`);
        return urlLang;
    }
    
    // 2. Check localStorage
    try {
        const storedLang = localStorage.getItem(LANG_CONFIG.storageKey);
        if (storedLang && LANG_CONFIG.supportedLangs.includes(storedLang)) {
            logDebug(`Language from localStorage: ${storedLang}`);
            return storedLang;
        }
    } catch (e) {
        logError('localStorage access failed', e);
    }
    
    // 3. Check browser language
    const browserLang = navigator.language.split('-')[0];
    if (LANG_CONFIG.supportedLangs.includes(browserLang)) {
        logDebug(`Language from browser: ${browserLang}`);
        return browserLang;
    }
    
    // 4. Fallback to default
    logDebug(`Using default language: ${LANG_CONFIG.defaultLang}`);
    return LANG_CONFIG.defaultLang;
}

function saveLanguage(lang) {
    try {
        localStorage.setItem(LANG_CONFIG.storageKey, lang);
        logDebug(`Language saved: ${lang}`);
    } catch (e) {
        logError('Failed to save language to localStorage', e);
    }
}

// ============================================
// 4. TRANSLATION LOADER (loads from external translations.js)
// ============================================
let translationsData = null;

function loadTranslationsSync() {
    if (typeof translations !== 'undefined') {
        translationsData = translations;
        logDebug('Translations loaded successfully', {
            languages: Object.keys(translationsData),
            totalKeys: Object.keys(translationsData.en || {}).length
        });
        return true;
    } else {
        logError('translations.js not loaded! Make sure it is included BEFORE language-v3.js');
        return false;
    }
}

// ============================================
// 5. TRANSLATION FUNCTION WITH FALLBACK
// ============================================
function translate(key, lang) {
    if (!translationsData) {
        logError('Translations not loaded');
        return key;
    }
    
    // Try requested language
    if (translationsData[lang] && translationsData[lang][key]) {
        return translationsData[lang][key];
    }
    
    // Fallback chain
    for (const fallbackLang of LANG_CONFIG.fallbackChain) {
        if (fallbackLang !== lang && translationsData[fallbackLang] && translationsData[fallbackLang][key]) {
            logDebug(`Fallback used: ${lang} → ${fallbackLang} for key "${key}"`);
            return translationsData[fallbackLang][key];
        }
    }
    
    // If still not found, try English
    if (translationsData.en && translationsData.en[key]) {
        logDebug(`Final fallback to EN for key "${key}"`);
        return translationsData.en[key];
    }
    
    // No translation found
    logError(`Missing translation for key: "${key}" in language: ${lang}`);
    return key; // Return the key itself as last resort
}

// ============================================
// 6. PAGE TRANSLATION
// ============================================
function translatePage(lang) {
    if (!translationsData) {
        logError('Cannot translate: translations not loaded');
        return;
    }
    
    logDebug(`Starting page translation to: ${lang}`);
    let translatedCount = 0;
    let missingCount = 0;
    const missingKeys = [];
    
    // Find all elements with data-i18n attribute
    const elements = document.querySelectorAll('[data-i18n]');
    logDebug(`Found ${elements.length} translatable elements`);
    
    elements.forEach((element, index) => {
        const key = element.getAttribute('data-i18n');
        const translatedText = translate(key, lang);
        
        if (translatedText !== key) {
            element.textContent = translatedText;
            translatedCount++;
            logDebug(`[${index + 1}/${elements.length}] ✓ ${key} → "${translatedText}"`);
        } else {
            missingCount++;
            missingKeys.push(key);
            logError(`[${index + 1}/${elements.length}] ✗ Missing: ${key}`);
            
            // Visual indicator for missing translations in debug mode
            if (LANG_CONFIG.debugMode) {
                element.style.color = 'red';
                element.style.border = '1px dashed red';
                element.title = `Missing translation: ${key}`;
            }
        }
    });
    
    logDebug('Translation complete', {
        language: lang,
        total: elements.length,
        translated: translatedCount,
        missing: missingCount,
        missingKeys: missingKeys
    });
    
    // Update HTML lang attribute
    document.documentElement.lang = lang;
}

// ============================================
// 7. LANGUAGE SWITCHER
// ============================================
function switchLanguage(newLang) {
    if (!LANG_CONFIG.supportedLangs.includes(newLang)) {
        logError(`Unsupported language: ${newLang}`);
        return;
    }
    
    logDebug(`Switching language to: ${newLang}`);
    
    // Save to localStorage
    saveLanguage(newLang);
    
    // Update URL without reload
    const url = new URL(window.location);
    url.searchParams.set('lang', newLang);
    window.history.replaceState({}, '', url);
    
    // Translate page
    translatePage(newLang);
    
    // Update active button styling
    updateLanguageButtons(newLang);
}

function updateLanguageButtons(activeLang) {
    const buttons = document.querySelectorAll('[data-lang]');
    buttons.forEach(btn => {
        const btnLang = btn.getAttribute('data-lang');
        if (btnLang === activeLang) {
            btn.classList.add('active');
            btn.style.opacity = '1';
            btn.style.fontWeight = 'bold';
        } else {
            btn.classList.remove('active');
            btn.style.opacity = '0.6';
            btn.style.fontWeight = 'normal';
        }
    });
}

// ============================================
// 8. INITIALIZATION
// ============================================
function initLanguageSystem() {
    logDebug('Initializing Language System v3...');
    
    // Load translations
    const loaded = loadTranslationsSync();
    if (!loaded) {
        logError('Failed to load translations. Aborting initialization.');
        return;
    }
    
    // Detect current language
    const currentLang = detectLanguage();
    logDebug(`Detected language: ${currentLang}`);
    
    // Translate page immediately
    translatePage(currentLang);
    
    // Update button states
    updateLanguageButtons(currentLang);
    
    // Attach event listeners to language buttons
    const langButtons = document.querySelectorAll('[data-lang]');
    logDebug(`Attaching listeners to ${langButtons.length} language buttons`);
    
    langButtons.forEach(btn => {
        const lang = btn.getAttribute('data-lang');
        btn.addEventListener('click', () => {
            logDebug(`Language button clicked: ${lang}`);
            switchLanguage(lang);
        });
    });
    
    logDebug('✓ Language System v3 initialized successfully');
}

// ============================================
// 9. MUTATION OBSERVER FOR DYNAMIC CONTENT
// ============================================
function observeDynamicContent() {
    logDebug('Starting MutationObserver for dynamic content...');
    
    const observer = new MutationObserver((mutations) => {
        let needsRetranslation = false;
        
        mutations.forEach((mutation) => {
            mutation.addedNodes.forEach((node) => {
                // Check if added node or its children have data-i18n
                if (node.nodeType === 1) { // Element node
                    if (node.hasAttribute && node.hasAttribute('data-i18n')) {
                        needsRetranslation = true;
                        logDebug('New translatable element detected:', node);
                    }
                    // Check children
                    if (node.querySelectorAll) {
                        const translatableChildren = node.querySelectorAll('[data-i18n]');
                        if (translatableChildren.length > 0) {
                            needsRetranslation = true;
                            logDebug(`New container with ${translatableChildren.length} translatable children detected`);
                        }
                    }
                }
            });
        });
        
        if (needsRetranslation) {
            const currentLang = detectLanguage();
            logDebug('Re-translating page due to DOM changes...');
            translatePage(currentLang);
            updateLanguageButtons(currentLang);
        }
    });
    
    // Observe the entire body for changes
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
    
    logDebug('MutationObserver active');
}

// ============================================
// 10. AUTO-START
// ============================================
if (document.readyState === 'loading') {
    // DOM not ready yet
    document.addEventListener('DOMContentLoaded', () => {
        initLanguageSystem();
        // Start observing AFTER initial translation
        setTimeout(() => observeDynamicContent(), 500);
    });
} else {
    // DOM already loaded
    initLanguageSystem();
    setTimeout(() => observeDynamicContent(), 500);
}

// ============================================
// 11. EXPOSE API FOR DEBUGGING
// ============================================
window.LanguageSystemV3 = {
    version: '3.1.0', // Updated version
    config: LANG_CONFIG,
    getCurrentLanguage: detectLanguage,
    switchLanguage: switchLanguage,
    translatePage: translatePage,
    getTranslations: () => translationsData,
    enableDebug: () => { LANG_CONFIG.debugMode = true; },
    disableDebug: () => { LANG_CONFIG.debugMode = false; }
};

logDebug('Language System v3.1 loaded with MutationObserver. Access via window.LanguageSystemV3');
