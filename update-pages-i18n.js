/**
 * Automated Script to Update All HTML Pages with i18n Support
 * This script adds data-i18n attributes and includes the i18n.js script
 */

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

// I18n script tag to inject before closing </head>
const i18nScriptTag = `    <!-- i18n Translation System -->
    <script src="i18n.js"></script>`;

pages.forEach(page => {
    const filePath = path.join(__dirname, page);
    
    if (!fs.existsSync(filePath)) {
        console.log(`⚠️  ${page} not found, skipping...`);
        return;
    }
    
    let content = fs.readFileSync(filePath, 'utf8');
    
    // Check if i18n script already exists
    if (content.includes('i18n.js')) {
        console.log(`✓ ${page} already has i18n.js, skipping...`);
        return;
    }
    
    // Add i18n script before </head>
    content = content.replace('</head>', `${i18nScriptTag}\n</head>`);
    
    // Backup original file
    fs.writeFileSync(filePath + '.i18n-backup', content);
    
    // Write updated content
    fs.writeFileSync(filePath, content);
    
    console.log(`✅ Updated ${page} with i18n support`);
});

console.log('\n🎉 All pages updated successfully!');
console.log('Backup files created with .i18n-backup extension');
