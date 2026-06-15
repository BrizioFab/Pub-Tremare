"""
TREMARE PUB - Web Showcase
Flask application for a waterfront pub in Baia, Naples
with boat delivery service.

Future features (placeholder):
- Reservation system with database (SQLAlchemy)
- Admin panel for menu management
- Real-time boat delivery orders tracking
- Customer reviews and ratings
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# ============================================================================
# ROUTES - HOME PAGE
# ============================================================================
@app.route('/')
def home():
    """Homepage with hero, featured menu items, and boat delivery teaser."""
    return render_template('index.html')

# ============================================================================
# ROUTES - MENU
# ============================================================================
@app.route('/menu')
def menu():
    """Complete menu with categories (cocktails, beer, food, etc)."""
    menu_data = {
        'cocktails': [
            {
                'name': 'Tremare Blu',
                'description': 'Rum, Blue Curaçao, succo di lime, decorazione di sale marino',
                'price': '€9'
            },
            {
                'name': 'Mare Nostro',
                'description': 'Vodka, sciroppo di riccio di mare, prosecco, ghiaccio',
                'price': '€10'
            },
            {
                'name': 'Baia Sunset',
                'description': 'Aperol, prosecco, acqua di soda, fetta di arancia',
                'price': '€8'
            },
            {
                'name': 'Mitologia',
                'description': 'Whisky, miele, limone, infuso di erbe mediterranee',
                'price': '€11'
            }
        ],
        'beer': [
            {
                'name': 'Birra Artigianale Locale',
                'description': 'Selezione di birre craft dal territorio campano',
                'price': '€5-7'
            },
            {
                'name': 'Birra Internazionale',
                'description': 'Pilsner, IPA, Stout da tutto il mondo',
                'price': '€6-8'
            }
        ],
        'food': [
            {
                'name': 'Pinsone al ragù',
                'description': 'Pane toscano con ragù napoletano lento',
                'price': '€8'
            },
            {
                'name': 'Bottoncini di baccalà',
                'description': 'Baccalà fritto con dip di aglio e peperoncino',
                'price': '€7'
            },
            {
                'name': 'Burrata e pomodori',
                'description': 'Burrata fresca con pomodori di collina e basilico',
                'price': '€9'
            },
            {
                'name': 'Mozzarella affumicata',
                'description': 'Mozzarella di bufala affumicata, tarallini, olio extravergine',
                'price': '€10'
            }
        ]
    }
    return render_template('menu.html', menu=menu_data)

# ============================================================================
# ROUTES - BOAT DELIVERY
# ============================================================================
@app.route('/boat-delivery')
def boat_delivery():
    """Information and order form for boat delivery service."""
    return render_template('boat_delivery.html')

# ============================================================================
# ROUTES - CONTACTS
# ============================================================================
@app.route('/contatti')
def contatti():
    """Contact information and location."""
    return render_template('contatti.html')

# ============================================================================
# API ENDPOINTS - Future Reservation System
# ============================================================================
# TODO: Implement with Flask-SQLAlchemy
# @app.route('/api/reservations', methods=['POST'])
# def create_reservation():
#     """
#     Create a new reservation.
#     Expected JSON:
#     {
#         'name': str,
#         'phone': str,
#         'email': str,
#         'date': str (YYYY-MM-DD),
#         'time': str (HH:MM),
#         'guests': int,
#         'notes': str (optional)
#     }
#     """
#     pass

# TODO: Implement with Flask-SQLAlchemy + Celery
# @app.route('/api/boat-order', methods=['POST'])
# def create_boat_order():
#     """
#     Create a boat delivery order.
#     Expected JSON:
#     {
#         'boat_name': str,
#         'items': [{'name': str, 'quantity': int}],
#         'location': str (lat/lng or description),
#         'phone': str,
#         'payment_method': str
#     }
#     """
#     pass

# ============================================================================
# ERROR HANDLERS
# ============================================================================
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors."""
    return render_template('500.html'), 500

# ============================================================================
# UTILITIES
# ============================================================================
@app.context_processor
def inject_config():
    """Inject common variables into all templates."""
    return {
        'pub_name': 'TREMARE',
        'whatsapp': '3770920451',
        'current_year': datetime.now().year,
        'location': 'Porto di Baia, Napoli',
        'phone': '+39 081 123 4567'  # TODO: Update with actual phone
    }

# ============================================================================
# MAIN
# ============================================================================
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
