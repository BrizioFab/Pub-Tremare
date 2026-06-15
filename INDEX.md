# 📑 INDEX - NAVIGAZIONE DEL PROGETTO TREMARE

Benvenuto al repository Tremare Pub! Questa pagina ti aiuta a navigare tutti i file e capire la struttura del progetto.

---

## 🚀 DOVE INIZIARE

### Se sei... un proprietario del pub
→ Leggi: **[DELIVERY_SUMMARY.md](DELIVERY_SUMMARY.md)** (5 min)  
Poi: Personalizza i dati in **app.py** e aggiungi immagini

### Se sei... uno sviluppatore
→ Leggi: **[README.md](README.md)** (10 min)  
Poi: Setup locale seguendo le istruzioni  
Poi: Leggi **[DEVELOPMENT.md](DEVELOPMENT.md)** per code guidelines

### Se sei... un designer
→ Leggi: **[DESIGN_SPECIFICATION.md](DESIGN_SPECIFICATION.md)** (20 min)  
Poi: Personalizza colori in **style.css** (:root variables)

### Se devi... deployare il sito
→ Leggi: **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** (completamente)  
Scegli tra Heroku, DigitalOcean, o AWS

---

## 📁 STRUTTURA FILE (14 file totali)

### 📖 DOCUMENTAZIONE (5 file)
```
README.md                     ← START HERE (overview completo)
├── Quick start
├── Descrizione pagine
├── Tech stack
└── Contact info

DESIGN_SPECIFICATION.md       ← Per designer/design decisions
├── Wireframe concettuale
├── Color psychology
├── Typography spec
├── Component specs
└── Responsive breakpoints

DEPLOYMENT_GUIDE.md           ← Per devops/hosting
├── Setup locale
├── Testing procedure
├── Deploy (Heroku, DigitalOcean, AWS)
├── Monitoring
└── Troubleshooting

DELIVERY_SUMMARY.md           ← Recap finale (quello che hai ricevuto)
├── File structure
├── Cosa è stato creato
├── Checklist
└── Prossimi step

DEVELOPMENT.md                ← Per manutentori (best practices)
├── Code guidelines
├── File naming
├── CSS structure
└── Git workflow
```

### 💻 BACKEND (1 file)
```
app.py (380 linee)
├── Flask initialization
├── Route definitions
│   ├── @app.route('/') → home()
│   ├── @app.route('/menu') → menu()
│   ├── @app.route('/boat-delivery') → boat_delivery()
│   ├── @app.route('/contatti') → contatti()
│   ├── @app.errorhandler(404)
│   └── @app.errorhandler(500)
├── Menu data (cocktail, beer, food)
├── Context processor (inject_config)
├── TODO comments per future features
└── Main entry point
```

### 🎨 FRONTEND HTML (7 file)

#### Base Template
```
templates/base.html (120 linee)
├── <!DOCTYPE html> structure
├── <head> (meta tags, CSS link)
├── <nav> (navbar sticky + hamburger mobile)
├── Floating WhatsApp button (always visible)
├── <main> {% block content %}
├── <footer> (info, orari, contatti)
└── JavaScript inclusion
```

#### Content Templates (all extend base.html)
```
templates/index.html (170 linee) — HOME PAGE
├── Hero section (logo + headline)
├── About section (3 highlights)
├── Featured menu (3 cards)
├── Boat delivery preview
└── Final CTA

templates/menu.html (100 linee) — MENU PAGE
├── Menu header
├── Category: Cocktail (4 items)
├── Category: Birra (2 items)
├── Category: Cibo (4 items)
├── Menu note
└── CTA

templates/boat_delivery.html (250 linee) — BOAT DELIVERY
├── Header
├── How it works (4 steps)
├── Service details (6 cards)
├── Order form section
├── Testimonials (3)
└── Final CTA

templates/contatti.html (200 linee) — CONTACTS
├── Header
├── Contact grid (6 cards)
├── Map embed
├── FAQ (6 items)
├── Newsletter signup
└── Links

templates/404.html (10 linee) — ERROR PAGE
└── Simple error message + home link

templates/500.html (10 linee) — SERVER ERROR
└── Error message + contact CTA
```

### 🎨 FRONTEND CSS (1 file)
```
static/css/style.css (2000+ linee)
├── :root variables (colori, font, spacing, shadows)
├── Reset & Base styles
├── Typography (h1-h6, p, a)
├── Layout utilities (.section-container)
├── Navbar styles
├── WhatsApp button (fixed, animated)
├── Buttons (.cta-button variants)
├── Hero section
├── About section
├── Featured menu
├── Boat delivery preview
├── Menu page specific
├── Boat delivery page specific
├── Contacts page specific
├── Final CTA section
├── Footer styles
├── Media queries
│   ├── @media (min-width: 768px) — Tablet
│   ├── @media (min-width: 1024px) — Desktop
│   └── @media print
└── Custom animations (bounce, etc)
```

### 📱 FRONTEND JS (1 file)
```
static/js/main.js (300 linee)
├── DOMContentLoaded event
├── initNavbarToggle()
│   ├── Toggle menu on button click
│   ├── Close menu on link click
│   └── Close menu on outside click
├── Smooth scroll for anchors
└── TODO comments per future features
    ├── Reservation system
    ├── Boat order tracking
    ├── Newsletter signup
    └── Analytics integration
```

### 📷 IMAGES (1 file)
```
static/img/logo.png
└── Copia di Logo.jpeg in PNG format (usata nei template)
```

### 🔧 CONFIG FILES (3 file)
```
requirements.txt
├── Flask==3.0.0
├── Werkzeug==3.0.1
├── python-dotenv==1.0.0
└── gunicorn==21.2.0

.env.example
├── FLASK_ENV=development
├── FLASK_DEBUG=True
├── SECRET_KEY=...
├── PUB_PHONE=...
└── WHATSAPP_NUMBER=...

.gitignore (se esiste)
├── venv/
├── __pycache__/
├── .env
├── *.pyc
└── .DS_Store
```

---

## 🔄 FILE RELATIONSHIPS

```
app.py
│
└─→ templates/base.html (parent per tutti)
    ├─→ templates/index.html
    ├─→ templates/menu.html
    ├─→ templates/boat_delivery.html
    ├─→ templates/contatti.html
    ├─→ templates/404.html
    └─→ templates/500.html

static/css/style.css
└─→ Incluso in base.html <head>

static/js/main.js
└─→ Incluso in base.html <body end>

static/img/logo.png
└─→ Usato in base.html e index.html
```

---

## 📊 STATISTICS

| Categoria | Files | Linee | Note |
|-----------|-------|-------|------|
| Backend | 1 | 380 | Flask app |
| Frontend HTML | 7 | 900 | All templates |
| Frontend CSS | 1 | 2000+ | All styling |
| Frontend JS | 1 | 300 | Interactivity |
| Config | 3 | 100 | Requirements, env, ignore |
| Documentation | 5 | 3500+ | Guides, specs |
| **TOTALE** | **18** | **7000+** | **Production ready** |

---

## 🎯 PAGINE E ROUTING

### Mappa delle pagine
```
/                       → home()           → templates/index.html
/menu                   → menu()           → templates/menu.html
/boat-delivery          → boat_delivery()  → templates/boat_delivery.html
/contatti               → contatti()       → templates/contatti.html
/non-esiste             → [404]            → templates/404.html
/errore-server          → [500]            → templates/500.html
```

### Navbar Navigation
```
[TREMARE] ← Home link (/)
├── Home (/)
├── Menù (/menu)
├── Consegna in Barca (/boat-delivery)
└── Contatti (/contatti)
```

### Footer Links
```
Footer
├── Sezione 1: Pub name & location
├── Sezione 2: Phone & WhatsApp
├── Sezione 3: Hours
└── Copyright notice
```

---

## 💡 COME MODIFICARE COSE

### Cambiare colore del tema
**File**: `static/css/style.css`  
**Cerca**: `:root {` (linea 5)  
**Modifica**: `--color-navy`, `--color-teal`, `--color-gold`, etc.

### Cambiare font
**File**: `templates/base.html` (aggiungere import in <head>)  
**Oppure**: Modificare `--font-serif` e `--font-sans` in style.css

### Aggiungere una nuova pagina
**Step 1**: Crea route in `app.py`
```python
@app.route('/new-page')
def new_page():
    return render_template('new_page.html')
```

**Step 2**: Crea template `templates/new_page.html`
```html
{% extends "base.html" %}
{% block title %}Page Title{% endblock %}
{% block content %}
<!-- Content here -->
{% endblock %}
```

**Step 3**: Aggiungi link in navbar (base.html)

### Aggiungere un item al menù
**File**: `app.py` (linea 40-80)  
**Modifica**: Il dizionario `menu_data` nella route `/menu`

### Cambiare numero WhatsApp
**File**: `app.py` (linea 85)  
**Cambia**: `whatsapp_number`

### Aggiungere una nuova sezione a home
**File**: `templates/index.html`  
**Step**: Aggiungi una nuova `<section class="section-name">` prima del footer

---

## 🔗 EXTERNAL LINKS

### Servizi Usati
- Flask 3.0: https://flask.palletsprojects.com/
- Jinja2: https://jinja.palletsprojects.com/
- Google Fonts: https://fonts.google.com/
  - Playfair Display: https://fonts.google.com/?query=playfair
  - Inter: https://fonts.google.com/?query=inter

### Deployment
- Heroku: https://www.heroku.com/
- DigitalOcean: https://www.digitalocean.com/
- AWS: https://aws.amazon.com/

### Resources
- Unsplash (free images): https://unsplash.com/
- Pexels (free images): https://pexels.com/
- FontAwesome (icons): https://fontawesome.com/

---

## ✅ QUICK CHECKLIST

- [ ] Leggi README.md
- [ ] Setup locale con `python app.py`
- [ ] Testa tutte 4 le pagine
- [ ] Aggiorna numero WhatsApp
- [ ] Aggiungi immagini reali
- [ ] Personalizza menù se diverso
- [ ] Test su mobile
- [ ] Deploy seguendo DEPLOYMENT_GUIDE.md
- [ ] Monitora con Google Analytics
- [ ] Raccogli feedback dagli utenti

---

## 🆘 TROUBLESHOOTING

### Il sito non si avvia
→ Vedi **DEPLOYMENT_GUIDE.md** sezione Troubleshooting

### Le immagini non caricano
→ Controlla path in template (deve essere `{{ url_for('static', filename='...') }}`)

### Navbar non si toglie su mobile
→ Controlla JavaScript in console (F12)

### Colori diversi dal mockup
→ Verifica `--color-*` variables in style.css `:root`

---

## 📞 SUPPORT

### Per problemi tecnici
Apri una Issue su GitHub o contatta lo sviluppatore

### Per miglioramenti
Vedi: **DELIVERY_SUMMARY.md** sezione "Suggerimenti per Miglioramenti Futuri"

### Per design customization
Vedi: **DESIGN_SPECIFICATION.md**

---

## 🎓 FILE READING ORDER

**Per il proprietario**:
1. DELIVERY_SUMMARY.md
2. app.py (riga 50-90)
3. .env.example

**Per lo sviluppatore**:
1. README.md
2. app.py
3. DESIGN_SPECIFICATION.md
4. DEVELOPMENT.md
5. static/css/style.css
6. static/js/main.js

**Per il designer**:
1. DESIGN_SPECIFICATION.md
2. static/css/style.css (`:root` variables)
3. templates/base.html

**Per il DevOps**:
1. DEPLOYMENT_GUIDE.md
2. requirements.txt
3. .env.example
4. app.py

---

**Ultimo aggiornamento**: June 15, 2024  
**Versione**: 1.0  
**Status**: Production Ready ✅
