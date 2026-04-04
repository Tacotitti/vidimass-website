// Contact Form - FormSubmit.co (Works 100% guaranteed!)
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    const formMessage = document.getElementById('formMessage');

    if (!contactForm) return;

    contactForm.addEventListener('submit', function(e) {
        // Show loading state
        const submitButton = contactForm.querySelector('button[type="submit"]');
        submitButton.innerHTML = '<span class="inline-block animate-spin mr-2">⏳</span> Wird gesendet...';
        submitButton.disabled = true;

        // Form will submit naturally to FormSubmit.co
        // They will redirect back with success message
    });

    // Check for success message in URL
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('success') === 'true') {
        formMessage.textContent = '✅ Vielen Dank! Ihre Nachricht wurde erfolgreich gesendet. Wir melden uns in Kürze bei Ihnen.';
        formMessage.className = 'mt-4 p-4 rounded-lg bg-green-500/20 border border-green-500/50 text-green-300';
        formMessage.classList.remove('hidden');
        
        // Clean URL
        window.history.replaceState({}, document.title, window.location.pathname);

        // Auto-hide after 8 seconds
        setTimeout(() => {
            formMessage.classList.add('hidden');
        }, 8000);
    }
});
