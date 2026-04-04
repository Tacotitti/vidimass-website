// Contact Form Handler - Direct Email via mailto (Works Immediately!)
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    const formMessage = document.getElementById('formMessage');

    if (!contactForm) return;

    contactForm.addEventListener('submit', async function(e) {
        e.preventDefault();

        // Get form data
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const category = document.getElementById('category').value;
        const message = document.getElementById('message').value.trim();

        // Category labels
        const categoryLabels = {
            'tiktok': 'TikTok Mass Posting',
            'spotify': 'Spotify Charting',
            'instagram': 'Instagram Mass Posting',
            'multi': 'Multi-Plattform',
            'label': 'Musik-Label/Artist Charting',
            'enterprise': 'Unternehmen',
            'other': 'Sonstiges'
        };

        // Create mailto link
        const subject = encodeURIComponent(`[MediaMass Kontakt] ${categoryLabels[category]} - ${name}`);
        const body = encodeURIComponent(`
Von: ${name}
E-Mail: ${email}
Kategorie: ${categoryLabels[category]}

Nachricht:
----------
${message}

==========================================
Gesendet über: www.masspost.store/contact.html
        `.trim());

        // Open default email client
        window.location.href = `mailto:info@masspost.store?subject=${subject}&body=${body}`;

        // Show success message
        showMessage('✅ Ihr E-Mail-Programm wurde geöffnet. Bitte senden Sie die vorgefertigte E-Mail ab. Alternativ: info@masspost.store', 'success');
        contactForm.reset();
    });

    function showMessage(message, type) {
        formMessage.textContent = message;
        formMessage.className = `mt-4 p-4 rounded-lg ${
            type === 'success' 
                ? 'bg-green-500/20 border border-green-500/50 text-green-300' 
                : 'bg-red-500/20 border border-red-500/50 text-red-300'
        }`;
        formMessage.classList.remove('hidden');

        // Scroll to message
        formMessage.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
});
