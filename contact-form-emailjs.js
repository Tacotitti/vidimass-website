// Contact Form Handler with EmailJS (Free 200 emails/month)
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    const formMessage = document.getElementById('formMessage');

    if (!contactForm) return;

    // Initialize EmailJS
    emailjs.init('JuX8vF9gKhO4L7mP2'); // MediaMass Public Key

    contactForm.addEventListener('submit', async function(e) {
        e.preventDefault();

        // Disable submit button
        const submitButton = contactForm.querySelector('button[type="submit"]');
        const originalButtonText = submitButton.innerHTML;
        submitButton.disabled = true;
        submitButton.innerHTML = '<span class="inline-block animate-spin mr-2">⏳</span> Wird gesendet...';

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

        // Template parameters for EmailJS
        const templateParams = {
            from_name: name,
            from_email: email,
            category: categoryLabels[category],
            message: message,
            to_email: 'info@masspost.store'
        };

        try {
            // Send via EmailJS
            const response = await emailjs.send(
                'service_masspost', // Service ID
                'template_contact', // Template ID
                templateParams
            );

            if (response.status === 200) {
                showMessage('✅ Vielen Dank! Ihre Nachricht wurde erfolgreich gesendet. Wir melden uns in Kürze bei Ihnen.', 'success');
                contactForm.reset();
            } else {
                showMessage('❌ Fehler beim Senden. Bitte versuchen Sie es erneut oder kontaktieren Sie uns direkt.', 'error');
            }
        } catch (error) {
            console.error('EmailJS error:', error);
            showMessage('❌ Fehler beim Senden. Bitte kontaktieren Sie uns direkt per E-Mail: info@masspost.store', 'error');
        } finally {
            // Re-enable button
            submitButton.disabled = false;
            submitButton.innerHTML = originalButtonText;
        }
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

        // Auto-hide success after 8 seconds
        if (type === 'success') {
            setTimeout(() => {
                formMessage.classList.add('hidden');
            }, 8000);
        }
    }
});
