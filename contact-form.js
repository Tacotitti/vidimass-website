// Contact Form Handler
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    const formMessage = document.getElementById('formMessage');

    if (!contactForm) return;

    contactForm.addEventListener('submit', async function(e) {
        e.preventDefault();

        // Get form data
        const formData = {
            name: document.getElementById('name').value.trim(),
            email: document.getElementById('email').value.trim(),
            category: document.getElementById('category').value,
            message: document.getElementById('message').value.trim()
        };

        // Validate
        if (!formData.name || !formData.email || !formData.category || !formData.message) {
            showMessage('Bitte füllen Sie alle Felder aus.', 'error');
            return;
        }

        // Disable submit button
        const submitButton = contactForm.querySelector('button[type="submit"]');
        const originalButtonText = submitButton.innerHTML;
        submitButton.disabled = true;
        submitButton.innerHTML = '<span class="inline-block animate-spin mr-2">⏳</span> Wird gesendet...';

        try {
            // Send to Cloudflare Worker
            const response = await fetch('https://contact.masspost.store/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();

            if (result.success) {
                showMessage('✅ Vielen Dank! Ihre Nachricht wurde erfolgreich gesendet. Wir melden uns in Kürze bei Ihnen.', 'success');
                contactForm.reset();
            } else {
                showMessage('❌ ' + (result.error || 'Fehler beim Senden. Bitte versuchen Sie es erneut.'), 'error');
            }
        } catch (error) {
            console.error('Form submission error:', error);
            showMessage('❌ Verbindungsfehler. Bitte kontaktieren Sie uns direkt per E-Mail: info@masspost.store', 'error');
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

        // Auto-hide after 8 seconds
        setTimeout(() => {
            formMessage.classList.add('hidden');
        }, 8000);
    }
});
