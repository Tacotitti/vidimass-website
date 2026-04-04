// Contact Form - Direct PHP Backend Email Sending
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
            // Send to PHP backend
            const response = await fetch('contact-submit.php', {
                method: 'POST',
                body: formData
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
