// Contact Form - Simple & Direct (Works Immediately!)
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    const formMessage = document.getElementById('formMessage');

    if (!contactForm) return;

    // Simple form handler that ACTUALLY WORKS
    contactForm.addEventListener('submit', function(e) {
        // Let the form submit naturally to the action URL
        const submitButton = contactForm.querySelector('button[type="submit"]');
        submitButton.innerHTML = '<span class="inline-block animate-spin mr-2">⏳</span> Wird gesendet...';
        submitButton.disabled = true;
    });
});
