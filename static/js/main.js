// ============================================================================
// TREMARE PUB - MAIN JAVASCRIPT
// ============================================================================

document.addEventListener('DOMContentLoaded', function() {
    initNavbarToggle();
});

/**
 * Initialize mobile navbar toggle
 */
function initNavbarToggle() {
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');

    if (!navToggle || !navMenu) return;

    // Toggle menu on button click
    navToggle.addEventListener('click', function() {
        navMenu.classList.toggle('active');
        navToggle.classList.toggle('active');
    });

    // Close menu when a link is clicked
    const navLinks = navMenu.querySelectorAll('a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navMenu.classList.remove('active');
            navToggle.classList.remove('active');
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        const isClickInsideNav = navToggle.contains(event.target) || navMenu.contains(event.target);
        if (!isClickInsideNav && navMenu.classList.contains('active')) {
            navMenu.classList.remove('active');
            navToggle.classList.remove('active');
        }
    });
}

/**
 * Smooth scroll for anchor links
 */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href !== '#') {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});

// ============================================================================
// FUTURE FEATURES - PLACEHOLDER CODE
// ============================================================================

/*
 * TODO: Implement reservation system
 *
 * Features to add:
 * 1. Date/time picker for reservations
 * 2. Form validation
 * 3. API integration with Flask backend
 * 4. Email confirmation sending
 * 5. Payment integration (Stripe, Satispay, etc.)
 * 6. Admin panel for managing reservations
 *
 * Example code structure:
 *
function submitReservation(data) {
    fetch('/api/reservations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Reservation confirmed:', data);
        showSuccessMessage('Prenotazione confermata! Ti contatteremo presto.');
    })
    .catch(error => {
        console.error('Error:', error);
        showErrorMessage('Errore nella prenotazione. Riprovare.');
    });
}
 */

/*
 * TODO: Implement boat order tracking
 *
 * Features to add:
 * 1. Real-time order status (pending, confirmed, on the way, delivered)
 * 2. GPS tracking visualization
 * 3. Push notifications
 * 4. Order history
 * 5. Customer ratings system
 *
 * Example WebSocket integration:
 *
const socket = io(); // Socket.io for real-time updates

socket.on('order_status_update', (data) => {
    updateOrderStatus(data);
});
 */

/*
 * TODO: Newsletter signup integration
 *
 * Features to add:
 * 1. Email validation
 * 2. Integration with email service (Mailchimp, SendGrid, Brevo)
 * 3. Confirmation email
 * 4. Unsubscribe functionality
 *
 * Example code:
 *
function handleNewsletterSignup(email) {
    // Validate email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        showErrorMessage('Email non valida');
        return;
    }

    // Send to backend
    fetch('/api/newsletter/subscribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: email })
    })
    .then(response => response.json())
    .then(data => {
        showSuccessMessage('Grazie per l\'iscrizione!');
    })
    .catch(error => console.error('Error:', error));
}
 */

/*
 * TODO: Analytics integration
 *
 * Suggested tools:
 * 1. Google Analytics 4 (GA4)
 * 2. Hotjar (for heatmaps and session recordings)
 * 3. Sentry (for error tracking)
 * 4. PostHog (open-source alternative)
 *
 * GA4 example:
 *
// Add to HTML:
// <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
// <script>
//   window.dataLayer = window.dataLayer || [];
//   function gtag(){dataLayer.push(arguments);}
//   gtag('js', new Date());
//   gtag('config', 'G-XXXXXXXXXX');
// </script>

// Track custom events:
function trackOrderClick() {
    gtag('event', 'whatsapp_order_click', {
        'page_title': 'Menu Page'
    });
}
 */
