// Contact Form Handler with Formspree
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    const formMessage = document.getElementById('formMessage');

    if (!contactForm) return;

    contactForm.addEventListener('submit', async function(e) {
        e.preventDefault();

        // Disable submit button
        const submitButton = contactForm.querySelector('button[type="submit"]');
        const originalButtonText = submitButton.innerHTML;
        submitButton.disabled = true;
        submitButton.innerHTML = '<span class="inline-block animate-spin mr-2">⏳</span> Wird gesendet...';

        // Get form data
        const formData = new FormData(contactForm);

        try {
            // Send directly to Formspree (FREE - 50 submissions/month)
            const response = await fetch('https://formspree.io/f/mvgoebdv', {
                method: 'POST',
                body: formData,
                headers: {
                    'Accept': 'application/json'
                }
            });

            if (response.ok) {
                showMessage('✅ Vielen Dank! Ihre Nachricht wurde erfolgreich gesendet. Wir melden uns in Kürze bei Ihnen.', 'success');
                contactForm.reset();
            } else {
                const data = await response.json();
                if (data.errors) {
                    showMessage('❌ ' + data.errors.map(error => error.message).join(', '), 'error');
                } else {
                    showMessage('❌ Fehler beim Senden. Bitte versuchen Sie es erneut.', 'error');
                }
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
