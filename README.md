# 🍺 TREMARE PUB - Sito Web Vetrina

**Tremare** è un pub di lusso situato nel porto di Baia (Napoli) con un servizio esclusivo di consegna in barca.

Questo repository contiene il **sito web vetrina completo**, mobile-first, realizzato con Flask, HTML, CSS e JavaScript.

---

## 📋 Contenuti

- ✅ **App Flask** con routing completo
- ✅ **Template HTML5** responsive e semantici
- ✅ **Design System** con colori, font, e componenti
- ✅ **CSS mobile-first** responsive fino a 4K
- ✅ **Pulsante WhatsApp** floating always-visible
- ✅ **Menù completo** con categorie (cocktail, birra, cibo)
- ✅ **Sezione Consegna in Barca** con come funziona
- ✅ **Pagina Contatti** con informazioni complete
- ✅ **JavaScript vanilla** per interattività
- ✅ **Commenti e TODO** per future estensioni

---

## 🎨 Design System

### Palette Colori
- **Navy (#1a3a52)** - Colore primario, eleganza e profondità
- **Teal (#2a5a72)** - Colore secondario, accentuato
- **Oro (#d4a574)** - Colore accento, lusso e distinzione
- **Crema (#f5f1e8)** - Background alternativo, calmezza
- **Verde WhatsApp (#25D366)** - CTA primario, call-to-action

### Typography
- **Headings**: Playfair Display (serif, elegante)
- **Body**: Inter (sans-serif, leggibile e moderna)

### Componenti Principali
- **Pulsanti CTA**: Verde WhatsApp (primario) e Navy (secondario)
- **Card Menù**: Gradient navy-teal con accenti oro
- **Navbar**: Sticky, mobile-toggle, sempre visible WhatsApp
- **Footer**: Navy con informazioni e orari

---

## 📁 Struttura Progetto

```
Pub Tremare/
├── app.py                          # Flask application principale
├── requirements.txt                # Dipendenze Python
├── .env.example                    # Variabili ambiente (copie come .env)
├── Logo.jpeg                       # Logo del brand
│
├── templates/                      # Template HTML (Jinja2)
│   ├── base.html                  # Template base con navbar/footer
│   ├── index.html                 # Home page
│   ├── menu.html                  # Pagina menù
│   ├── boat_delivery.html         # Consegna in barca
│   └── contatti.html              # Contatti e informazioni
│
├── static/
│   ├── css/
│   │   └── style.css              # Stylesheet principale (6000+ linee)
│   ├── js/
│   │   └── main.js                # JavaScript vanilla
│   └── img/
│       └── logo.png               # Logo (copia di Logo.jpeg)
│
└── README.md                       # Questo file
```

---

## 🚀 Quick Start

### 1. Setup Locale

```bash
# Clone o scarica il progetto
cd "Pub Tremare"

# Crea un virtual environment
python -m venv venv

# Attiva il venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Installa dipendenze
pip install -r requirements.txt

# Copia .env.example a .env
cp .env.example .env
```

### 2. Esegui il Server

```bash
python app.py
```

Visita: **http://localhost:5000**

### 3. Deploy in Produzione

```bash
# Con Gunicorn (production server)
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Con Docker (opzionale)
docker build -t tremare-pub .
docker run -p 5000:5000 tremare-pub
```

---

## 📄 Descrizione Pagine

### **Home (`/`)**
- Hero section con logo e mission
- Sezione "About" con highlights
- Specialità della casa (3 card)
- Preview consegna in barca
- CTA finale

### **Menù (`/menu`)**
- 4 sezioni: Cocktail, Birra, Cibo
- 11+ item descritti con prezzi
- Design card responsive
- Link al menù completo

### **Consegna in Barca (`/boat-delivery`)**
- Come funziona (4 step)
- 6 dettagli del servizio
- Form ordine WhatsApp
- Testimonial (fake placeholder)
- Info zone e pagamenti

### **Contatti (`/contatti`)**
- 6 contact card (WhatsApp, Phone, Location, Hours, Email, Social)
- Mappa embedded Google Maps
- FAQ con 6 domande comuni
- Newsletter signup (future)

---

## 🎯 Design Decisions

### Mobile-First Approach
- CSS di base ottimizzato per smartphone
- Layout singola colonna per mobile
- Media query per tablet (768px) e desktop (1024px)
- Touch-friendly buttons (min 44px)

### Accessibility
- Semantica HTML5 (header, nav, main, footer, section, article)
- Alt text su immagini
- Color contrast conforme WCAG AA
- Aria labels su pulsanti

### Performance
- CSS inline nel style.css (niente import esterni)
- Google Fonts importate via link (CDN-ready)
- Immagini placeholder (da sostituire con vere immagini)
- Niente JavaScript pesante, vanilla JS solo

### UX Principles
- Hero section chiara con CTA primario
- Pulsante WhatsApp sempre visible
- Menù organizzato per categorie
- Sezione "Come funziona" step-by-step
- Social proof (testimonial sulla boat delivery)

---

## 🔮 Future Features (TODO)

### Backend Database
```python
# SQLAlchemy + Flask-SQLAlchemy per:
- Model Reservation (date, guests, notes)
- Model BoatOrder (items, location, status)
- Model MenuCategory & MenuItem
- Model Review & Rating
```

### Reservation System
- Datepicker integrato
- Calcolo disponibilità
- Conferma email
- Reminder SMS/Email

### Boat Order Tracking
- Real-time order status
- GPS tracking della consegna
- Notifiche push
- Order history per utente

### Admin Panel
- Dashboard vendite/ordini
- Gestione menù
- Analytics e report
- Gestione prenotazioni

### Payment Integration
- Stripe per carte di credito
- Satispay per mobile
- Paypal
- Bonifico bancario

### Email & Communication
- SendGrid/Brevo per email
- Twilio per SMS
- Push notification con Firebase
- Chatbot WhatsApp Business API

### Analytics
- Google Analytics 4
- Hotjar per heatmap
- Sentry per error tracking

### SEO & Marketing
- Meta tag e Open Graph
- Sitemap e robots.txt
- Schema markup (LocalBusiness)
- Google Business Profile sync

---

## 📊 Content & Copy

### Tono
- Moderno, fresco, marino
- Professionale ma amichevole
- Orientato alla conversione
- Testi brevi e incisivi

### Menù
Cocktail artigianali creati dal nostro bartender:
- Tremare Blu (Rum, Blue Curaçao, lime) - €9
- Mare Nostro (Vodka, riccie di mare, prosecco) - €10
- Baia Sunset (Aperol, prosecco, arancia) - €8
- Mitologia (Whisky, miele, limone, erbe) - €11

Birra:
- Artigianale locale - €5-7
- Internazionale - €6-8

Cibo:
- Pinsone al ragù - €8
- Bottoncini di baccalà - €7
- Burrata e pomodori - €9
- Mozzarella affumicata - €10

### Contact Info (TODO - Aggiorna con dati reali)
- **Phone**: +39 081 123 4567 (CHANGE)
- **WhatsApp**: 377 092 0451
- **Location**: Porto di Baia, Napoli
- **Hours**: 
  - Lun-Gio: 17:00 - 02:00
  - Ven-Sab: 17:00 - 03:00
  - Dom: 17:00 - 02:00

---

## 🖼️ Immagini Placeholder

### Descrizioni per Image Stock
1. **Logo**: Circular maritime badge with "TREMARE", "LA CITTÀ SOMMERSA"
2. **Hero Background**: Baia sunset, imbarcazioni nel porto
3. **Cocktail**: Colorful craft cocktail with maritime garnish
4. **Birra**: Cold beer glass con foam, tavolo con vista mare
5. **Cibo**: Burrata con pomodori, basil, olive oil
6. **Porto**: Aerial view di Baia con barche ancorate
7. **Team**: Bartender dietro il bancone, smile, vista mare dietro

**Risorse Free**:
- Unsplash, Pexels, Pixabay per immagini stock
- Canva per mock-up
- Figma per preview

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Flask 3.0 |
| **Frontend** | HTML5, CSS3, Vanilla JS |
| **Hosting** | AWS, Heroku, DigitalOcean |
| **Database** | PostgreSQL (future) |
| **Payment** | Stripe, Satispay (future) |
| **Email** | SendGrid, Brevo (future) |
| **Analytics** | Google Analytics 4 |

---

## 📈 SEO & Marketing

### Meta Tags
```html
<title>Tremare Pub - Baia, Napoli - Cocktail & Consegna in Barca</title>
<meta name="description" content="Cocktail artigianali e consegna direttamente sulla tua barca nel porto di Baia, Napoli.">
```

### Local SEO
- Google Business Profile listing
- Baia, Naples location
- Phone, hours, website
- Customer reviews

### Social Media
- Instagram: Behind-the-scenes, cocktail pics, sunset views
- Facebook: Events, specials, customer photos
- TikTok: Bartender skills, boat delivery moments, parties

---

## 🤝 Contributing

Per suggerimenti o miglioramenti, apri una Issue o invia una Pull Request.

---

## 📞 Support

Per domande tecniche sul sito web, contatta il web developer.
Per informazioni sul pub, contatta Tremare direttamente:
- **WhatsApp**: 377 092 0451
- **Phone**: +39 081 123 4567

---

## 📜 License

© 2024 Tremare Pub. Tutti i diritti riservati.

"La città sommersa" - Porto di Baia, Napoli.
