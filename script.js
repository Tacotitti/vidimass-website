// VIDIMASS Modern - JavaScript Interactions

document.addEventListener('DOMContentLoaded', function() {
    
    // ============================================
    // Mobile Menu Toggle
    // ============================================
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const body = document.body;
    
    // Create mobile menu and overlay if they don't exist
    if (!document.querySelector('.mobile-menu')) {
        const mobileMenu = document.createElement('div');
        mobileMenu.className = 'mobile-menu';
        mobileMenu.innerHTML = `
            <a href="#features">Features</a>
            <a href="#stats">Stats</a>
            <a href="#packages">Packages</a>
            <button class="w-full mt-4 px-6 py-3 bg-gradient-to-r from-violet-600 to-pink-600 rounded-full font-semibold hover:shadow-lg transition-all">
                Get Started
            </button>
        `;
        body.appendChild(mobileMenu);
        
        const overlay = document.createElement('div');
        overlay.className = 'mobile-overlay';
        body.appendChild(overlay);
        
        // Mobile menu toggle functionality
        mobileMenuToggle.addEventListener('click', function() {
            mobileMenu.classList.toggle('active');
            overlay.classList.toggle('active');
        });
        
        // Close menu when clicking overlay
        overlay.addEventListener('click', function() {
            mobileMenu.classList.remove('active');
            overlay.classList.remove('active');
        });
        
        // Close menu when clicking links
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function() {
                mobileMenu.classList.remove('active');
                overlay.classList.remove('active');
            });
        });
    }
    
    // ============================================
    // Smooth Scroll with Offset for Fixed Nav
    // ============================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offsetTop = target.offsetTop - 80; // Offset for fixed nav
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // ============================================
    // Navbar Background on Scroll
    // ============================================
    const nav = document.querySelector('nav');
    let lastScrollY = window.scrollY;
    
    window.addEventListener('scroll', function() {
        const currentScrollY = window.scrollY;
        
        if (currentScrollY > 100) {
            nav.style.background = 'rgba(15, 15, 26, 0.8)';
            nav.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)';
        } else {
            nav.style.background = 'rgba(15, 15, 26, 0.3)';
            nav.style.boxShadow = 'none';
        }
        
        lastScrollY = currentScrollY;
    });
    
    // ============================================
    // Scroll Reveal Animation
    // ============================================
    const observerOptions = {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, observerOptions);
    
    // Observe all cards and sections
    document.querySelectorAll('.stat-card, .feature-card, .package-card').forEach(el => {
        el.classList.add('scroll-reveal');
        observer.observe(el);
    });
    
    // ============================================
    // Number Counter Animation for Stats
    // ============================================
    function animateCounter(element, target, duration = 2000) {
        let start = 0;
        const increment = target / (duration / 16);
        const isK = target >= 1000;
        
        const timer = setInterval(() => {
            start += increment;
            if (start >= target) {
                start = target;
                clearInterval(timer);
            }
            
            if (isK) {
                element.textContent = Math.floor(start / 1000) + 'K+';
            } else {
                element.textContent = Math.floor(start) + '+';
            }
        }, 16);
    }
    
    // Trigger counter animation when stats section is visible
    const statsObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.dataset.animated) {
                entry.target.dataset.animated = 'true';
                
                const statCards = entry.target.querySelectorAll('.stat-card > div:first-child');
                if (statCards[0]) animateCounter(statCards[0], 250000, 2000);
                if (statCards[1]) animateCounter(statCards[1], 2, 1000);
                // Keep "24/7" as text, no counter needed
            }
        });
    }, { threshold: 0.3 });
    
    const statsSection = document.querySelector('.stats-section');
    if (statsSection) {
        statsObserver.observe(statsSection);
    }
    
    // ============================================
    // CTA Button Interactions
    // ============================================
    document.querySelectorAll('.cta-primary, .cta-button, .cta-secondary').forEach(button => {
        button.addEventListener('click', function(e) {
            // Ripple effect
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.style.position = 'absolute';
            ripple.style.borderRadius = '50%';
            ripple.style.background = 'rgba(255, 255, 255, 0.5)';
            ripple.style.transform = 'scale(0)';
            ripple.style.animation = 'ripple 0.6s ease-out';
            ripple.style.pointerEvents = 'none';
            
            this.appendChild(ripple);
            
            setTimeout(() => ripple.remove(), 600);
            
            // Handle button action (placeholder)
            console.log('CTA clicked:', this.textContent.trim());
        });
    });
    
    // Add ripple animation to CSS dynamically
    if (!document.querySelector('#ripple-animation')) {
        const style = document.createElement('style');
        style.id = 'ripple-animation';
        style.textContent = `
            @keyframes ripple {
                to {
                    transform: scale(4);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }
    
    // ============================================
    // Parallax Effect on Hero Section
    // ============================================
    const heroSection = document.querySelector('.hero-section');
    const floatingOrbs = document.querySelectorAll('.floating-orb');
    
    window.addEventListener('scroll', function() {
        const scrolled = window.scrollY;
        
        if (heroSection && scrolled < window.innerHeight) {
            floatingOrbs.forEach((orb, index) => {
                const speed = 0.3 + (index * 0.1);
                orb.style.transform = `translateY(${scrolled * speed}px)`;
            });
        }
    });
    
    // ============================================
    // Package Card Hover Effects
    // ============================================
    document.querySelectorAll('.package-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.boxShadow = '0 30px 60px rgba(139, 92, 246, 0.3)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.boxShadow = '';
        });
    });
    
    // ============================================
    // Feature Card Icon Animation
    // ============================================
    document.querySelectorAll('.feature-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            const icon = this.querySelector('svg');
            if (icon) {
                icon.style.transform = 'scale(1.2) rotate(5deg)';
                icon.style.transition = 'transform 0.3s ease';
            }
        });
        
        card.addEventListener('mouseleave', function() {
            const icon = this.querySelector('svg');
            if (icon) {
                icon.style.transform = 'scale(1) rotate(0deg)';
            }
        });
    });
    
    // ============================================
    // Page Load Animation
    // ============================================
    window.addEventListener('load', function() {
        body.classList.remove('loading');
        
        // Trigger hero animations
        const heroTitle = document.querySelector('.hero-title');
        if (heroTitle) {
            heroTitle.style.opacity = '0';
            setTimeout(() => {
                heroTitle.style.transition = 'opacity 1s ease, transform 1s ease';
                heroTitle.style.opacity = '1';
                heroTitle.style.transform = 'translateY(0)';
            }, 100);
        }
    });
    
    // ============================================
    // Easter Egg: Konami Code
    // ============================================
    let konamiCode = [];
    const konamiPattern = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
    
    document.addEventListener('keydown', function(e) {
        konamiCode.push(e.key);
        konamiCode = konamiCode.slice(-konamiPattern.length);
        
        if (JSON.stringify(konamiCode) === JSON.stringify(konamiPattern)) {
            activateEasterEgg();
        }
    });
    
    function activateEasterEgg() {
        const orbs = document.querySelectorAll('.floating-orb');
        orbs.forEach(orb => {
            orb.style.animation = 'float 2s infinite ease-in-out, rainbow 3s infinite';
        });
        
        // Add rainbow animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes rainbow {
                0% { filter: hue-rotate(0deg) blur(80px); }
                100% { filter: hue-rotate(360deg) blur(80px); }
            }
        `;
        document.head.appendChild(style);
        
        console.log('🎉 Easter Egg Activated! Rainbow mode enabled!');
    }
    
    // ============================================
    // Performance: Lazy Load Images (if any added later)
    // ============================================
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    observer.unobserve(img);
                }
            });
        });
        
        document.querySelectorAll('img.lazy').forEach(img => {
            imageObserver.observe(img);
        });
    }
    
    // ============================================
    // Console Art
    // ============================================
    console.log('%c VIDIMASS ', 'background: linear-gradient(90deg, #8b5cf6, #ec4899); color: white; font-size: 24px; font-weight: bold; padding: 10px;');
    console.log('%c Modern Website by Fred 🚀 ', 'background: #1f2937; color: #a855f7; font-size: 14px; padding: 5px;');
    console.log('%c Try the Konami Code! ⬆️⬆️⬇️⬇️⬅️➡️⬅️➡️BA ', 'color: #6b7280; font-size: 12px;');
});
