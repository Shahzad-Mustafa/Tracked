/* Portfolio — main.js */

document.addEventListener('DOMContentLoaded', () => {
    initScrollAnimations();
    initActiveNavLink();
    initAutoDismissAlerts();
    initThemeToggle();
});

/* Scroll-in animations with stagger for grid siblings */
function initScrollAnimations() {
    const els = document.querySelectorAll('.animate-on-scroll');
    if (!els.length) return;

    /* Stagger siblings inside the same .row that don't already have a delay */
    document.querySelectorAll('.row').forEach(row => {
        const children = [...row.querySelectorAll(':scope > .animate-on-scroll, :scope > [class*="col"] > .animate-on-scroll')];
        children.forEach((el, i) => {
            if (!el.style.transitionDelay) {
                el.style.transitionDelay = `${i * 0.09}s`;
            }
        });
    });

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.08 });

    els.forEach(el => observer.observe(el));
}

/* Highlight the nav link whose section is in view */
function initActiveNavLink() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-scroll');
    if (!sections.length || !navLinks.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                navLinks.forEach(link => {
                    link.classList.toggle(
                        'active',
                        link.getAttribute('href') === '#' + entry.target.id
                    );
                });
            }
        });
    }, { rootMargin: '-40% 0px -55% 0px' });

    sections.forEach(section => observer.observe(section));
}

/* Auto-dismiss success alert after 4 s */
function initAutoDismissAlerts() {
    const alert = document.getElementById('auto-dismiss-alert');
    if (!alert) return;
    setTimeout(() => {
        const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
        bsAlert.close();
    }, 4000);
}

/* Light / Dark theme toggle with localStorage persistence */
function initThemeToggle() {
    const btn = document.getElementById('theme-toggle-btn');
    if (!btn) return;

    const iconEl = btn.querySelector('.theme-icon');

    function applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('portfolio-theme', theme);
        if (iconEl) {
            iconEl.className = 'theme-icon bi ' + (theme === 'dark' ? 'bi-sun-fill' : 'bi-moon-stars-fill');
        }
        btn.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
        btn.setAttribute('title',      theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    }

    btn.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme') || 'light';
        applyTheme(current === 'dark' ? 'light' : 'dark');
    });

    /* Sync icon to whatever theme was already applied by the inline script */
    const saved = localStorage.getItem('portfolio-theme') ||
        (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    if (iconEl) {
        iconEl.className = 'theme-icon bi ' + (saved === 'dark' ? 'bi-sun-fill' : 'bi-moon-stars-fill');
    }
    btn.setAttribute('aria-label', saved === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    btn.setAttribute('title',      saved === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
}
