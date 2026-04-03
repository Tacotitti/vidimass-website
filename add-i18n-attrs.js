const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

// Navigation links
html = html.replace(/(<a href="#features"[^>]*>)Features(<\/a>)/g, '$1<span data-i18n="nav_features">Features</span>$2');
html = html.replace(/(<a href="#stats"[^>]*>)Stats(<\/a>)/g, '$1<span data-i18n="nav_stats">Stats</span>$2');
html = html.replace(/(<a href="#packages"[^>]*>)Packages(<\/a>)/g, '$1<span data-i18n="nav_packages">Packages</span>$2');

// Navigation button
html = html.replace(/(class="cta-button[^>]*>[\s\n]*)(Get Started)([\s\n]*<\/button>)/g, '$1<span data-i18n="nav_get_started">Get Started</span>$3');

// Hero badge
html = html.replace(/(<span class="text-sm text-gray-300">)24\/7 Distribution Active(<\/span>)/g, '$1<span data-i18n="hero_badge">24/7 Distribution Active</span>$2');

// Hero titles - need to preserve gradient classes
html = html.replace(/(<span class="bg-gradient-to-r from-violet-400 via-fuchsia-400 to-pink-400 bg-clip-text text-transparent">[\s\n]*)Mass Video Posting([\s\n]*<\/span>)/g, '$1<span data-i18n="hero_title_1">Mass Video Posting</span>$2');
html = html.replace(/(<span class="text-white">)At Scale(<\/span>)/g, '$1<span data-i18n="hero_title_2">At Scale</span>$2');

// Hero subtitle
html = html.replace(/(<p class="text-xl md:text-2xl text-gray-300 mb-12[^>]*>)Distribute up to <span class="font-bold text-violet-400">250,000 videos daily<\/span> across TikTok, Instagram, and multiple platforms with enterprise-grade automation\.(<\/p>)/g, '$1<span data-i18n="hero_subtitle">Distribute up to <strong>250,000 videos daily</strong> across TikTok, Instagram, and multiple platforms with enterprise-grade automation.</span>$2');

// Hero CTAs
html = html.replace(/(class="cta-primary[^>]*>[\s\n]*)Get Started Now([\s\n]*<\/button>)/g, '$1<span data-i18n="hero_cta_primary">Get Started Now</span>$2');
html = html.replace(/(class="cta-secondary[^>]*>[\s\n]*)View Packages([\s\n]*<\/button>)/g, '$1<span data-i18n="hero_cta_secondary">View Packages</span>$2');

// Trust indicators
html = html.replace(/(<span>)Enterprise Security(<\/span>)/g, '$1<span data-i18n="hero_trust_1">Enterprise Security</span>$2');
html = html.replace(/(<span>)99\.9% Uptime(<\/span>)/g, '$1<span data-i18n="hero_trust_2">99.9% Uptime</span>$2');
html = html.replace(/(<span>)24\/7 Support(<\/span>)/g, '$1<span data-i18n="hero_trust_3">24/7 Support</span>$2');

// Stats section
html = html.replace(/(<div class="text-5xl md:text-6xl font-bold bg-gradient-to-r from-violet-400 to-pink-400 bg-clip-text text-transparent mb-2">[\s\n]*)250K\+([\s\n]*<\/div>)/g, '$1<span data-i18n="stats_videos_count">250K+</span>$2');
html = html.replace(/(<div class="text-gray-300 text-lg">)Videos Per Day(<\/div>)/g, '$1<span data-i18n="stats_videos_label">Videos Per Day</span>$2');
html = html.replace(/(<div class="text-gray-500 text-sm mt-2">)Maximum Distribution Capacity(<\/div>)/g, '$1<span data-i18n="stats_videos_desc">Maximum Distribution Capacity</span>$2');

html = html.replace(/(<div class="text-5xl md:text-6xl font-bold bg-gradient-to-r from-violet-400 to-pink-400 bg-clip-text text-transparent mb-2">[\s\n]*)2\+([\s\n]*<\/div>)/g, '$1<span data-i18n="stats_platforms_count">2+</span>$2');
html = html.replace(/(<div class="text-gray-300 text-lg">)Platforms(<\/div>)/g, '$1<span data-i18n="stats_platforms_label">Platforms</span>$2');
html = html.replace(/(<div class="text-gray-500 text-sm mt-2">)TikTok, Instagram & More(<\/div>)/g, '$1<span data-i18n="stats_platforms_desc">TikTok, Instagram & More</span>$2');

html = html.replace(/(<div class="text-5xl md:text-6xl font-bold bg-gradient-to-r from-violet-400 to-pink-400 bg-clip-text text-transparent mb-2">[\s\n]*)24\/7([\s\n]*<\/div>)/g, '$1<span data-i18n="stats_distribution_count">24/7</span>$2');
html = html.replace(/(<div class="text-gray-300 text-lg">)Distribution(<\/div>)/g, '$1<span data-i18n="stats_distribution_label">Distribution</span>$2');
html = html.replace(/(<div class="text-gray-500 text-sm mt-2">)Automated & Always Active(<\/div>)/g, '$1<span data-i18n="stats_distribution_desc">Automated & Always Active</span>$2');

// Features section title
html = html.replace(/(<span class="bg-gradient-to-r from-violet-400 to-pink-400 bg-clip-text text-transparent">[\s\n]*)Enterprise-Grade([\s\n]*<\/span>)/g, '$1<span data-i18n="features_title_1">Enterprise-Grade</span>$2');
html = html.replace(/(<\/span>[\s\n]*) Features([\s\n]*<\/h2>)/g, '$1<span data-i18n="features_title_2"> Features</span>$2');
html = html.replace(/(<p class="text-xl text-gray-400 max-w-2xl mx-auto">)Built for creators and brands who need massive scale and reliability(<\/p>)/g, '$1<span data-i18n="features_subtitle">Built for creators and brands who need massive scale and reliability</span>$2');

// Individual features (1-6)
const features = [
    { title: 'Lightning Fast', desc: 'Upload and distribute thousands of videos in minutes, not hours.' },
    { title: 'Secure & Reliable', desc: 'Enterprise-grade security with 99.9% uptime guarantee.' },
    { title: 'Analytics Dashboard', desc: 'Track performance across all platforms in real-time.' },
    { title: 'Smart Scheduling', desc: 'AI-powered optimal posting times for maximum reach.' },
    { title: 'Multi-Account', desc: 'Manage unlimited accounts from one dashboard.' },
    { title: 'API Access', desc: 'Full API for custom integrations and automation.' }
];

features.forEach((feature, index) => {
    const i = index + 1;
    html = html.replace(
        new RegExp(`(<h3 class="text-xl font-bold mb-2">)${feature.title}(<\\/h3>)`, 'g'),
        `$1<span data-i18n="feature_${i}_title">${feature.title}</span>$2`
    );
    html = html.replace(
        new RegExp(`(<p class="text-gray-400">)${feature.desc.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}(<\\/p>)`, 'g'),
        `$1<span data-i18n="feature_${i}_desc">${feature.desc}</span>$2`
    );
});

// Packages section
html = html.replace(/(Choose Your <span class="bg-gradient-to-r from-violet-400 to-pink-400 bg-clip-text text-transparent">)Package(<\/span>)/g, '$1<span data-i18n="packages_title_2">Package</span>$2');
html = html.replace(/(<h2[^>]*>)Choose Your/g, '$1<span data-i18n="packages_title_1">Choose Your</span>');
html = html.replace(/(<p class="text-xl text-gray-400 max-w-2xl mx-auto">)Flexible plans that scale with your needs(<\/p>)/g, '$1<span data-i18n="packages_subtitle">Flexible plans that scale with your needs</span>$2');

// Footer
html = html.replace(/(<a href="#"[^>]*>)Privacy Policy(<\/a>)/g, '$1<span data-i18n="footer_privacy">Privacy Policy</span>$2');
html = html.replace(/(<a href="#"[^>]*>)Terms of Service(<\/a>)/g, '$1<span data-i18n="footer_terms">Terms of Service</span>$2');
html = html.replace(/(<a href="#"[^>]*>)Contact(<\/a>)/g, '$1<span data-i18n="footer_contact">Contact</span>$2');
html = html.replace(/(<div class="text-gray-500 text-sm">)© 2026 MediaMass\. All rights reserved\.(<\/div>)/g, '$1<span data-i18n="footer_copyright">© 2026 MediaMass. All rights reserved.</span>$2');

// Write the modified HTML
fs.writeFileSync('index.html', html);
console.log('✅ Successfully added data-i18n attributes to index.html');
