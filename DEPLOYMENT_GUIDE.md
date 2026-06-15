# GUIDA DI SETUP E DEPLOYMENT - TREMARE PUB

## 📋 Prerequisiti

- **Python 3.9+** (Check: `python --version`)
- **pip** package manager (Check: `pip --version`)
- **Git** (Check: `git --version`)
- **Un editor di testo** (VS Code consigliato)

---

## 🖥️ SETUP LOCALE

### Step 1: Clona o scarica il repository

```bash
# Se usi Git:
git clone <repository-url>
cd "Pub Tremare"

# Oppure scarica il file .zip e decomprimilo
cd "Pub Tremare"
```

### Step 2: Crea un Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

Dopo l'attivazione, dovresti vedere `(venv)` nel tuo terminale.

### Step 3: Installa le dipendenze

```bash
pip install -r requirements.txt
```

### Step 4: Configura le variabili d'ambiente

```bash
# Copia il file di esempio
cp .env.example .env

# Edita .env con i tuoi valori:
# - WHATSAPP_NUMBER=3770920451
# - PUB_PHONE=+39 081 123 4567
# - Etc.
```

### Step 5: Avvia il server di sviluppo

```bash
python app.py
```

Output atteso:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

Visita: **http://localhost:5000** nel tuo browser.

### Step 6: Stop del server

```bash
Ctrl + C
```

---

## 🧪 TEST LOCALE

### Verifica tutte le pagine

- [ ] Home: `http://localhost:5000/`
- [ ] Menù: `http://localhost:5000/menu`
- [ ] Consegna Barca: `http://localhost:5000/boat-delivery`
- [ ] Contatti: `http://localhost:5000/contatti`
- [ ] 404 Error: `http://localhost:5000/non-esiste`

### Verifica funzionalità

- [ ] Pulsante WhatsApp floating visibile
- [ ] Navbar mobile hamburger menu
- [ ] WhatsApp links correttamente formattati
- [ ] Responsive design (apri DevTools: F12 → Toggle device)
- [ ] Footer visibile su ogni pagina
- [ ] Tutti i link funzionano

### Test su Devices Reali

```bash
# Ottieni il tuo IP locale:
# Windows: ipconfig | findstr "IPv4"
# Mac: ifconfig | grep "inet "

# Accedi da mobile nella stessa rete:
http://<YOUR_IP>:5000
```

---

## 🚀 DEPLOYMENT IN PRODUZIONE

### Opzione 1: Heroku (Consigliato per principianti)

#### 1.1 Crea account su Heroku
- Visita: https://www.heroku.com
- Sign up (gratuito con limitazioni)
- Verifica email

#### 1.2 Installa Heroku CLI
```bash
# Windows: Scarica l'installer da https://devcenter.heroku.com/articles/heroku-cli
# Oppure: choco install heroku-cli

# Verifica:
heroku --version
```

#### 1.3 Login a Heroku
```bash
heroku login
```

#### 1.4 Crea un Procfile
```bash
# Nella root del progetto, crea file "Procfile" (no estensione)
echo "web: gunicorn -w 4 -b 0.0.0.0:\$PORT app:app" > Procfile
```

#### 1.5 Deploy
```bash
# Crea app Heroku
heroku create tremare-pub

# Deployment
git push heroku main

# Verifica logs
heroku logs --tail
```

**URL**: `https://tremare-pub.herokuapp.com`

### Opzione 2: DigitalOcean (Più scalabile)

#### 2.1 Crea account DigitalOcean
- Visita: https://www.digitalocean.com
- Aggiungi metodo di pagamento

#### 2.2 Crea un Droplet
- **Image**: Ubuntu 22.04 LTS
- **Size**: Basic ($6/month minimum)
- **Region**: Frankfurt o Amsterdam (più vicino all'Italia)
- **Authentication**: SSH key (consigliato)

#### 2.3 SSH nel server
```bash
ssh root@<your-droplet-ip>
```

#### 2.4 Setup server
```bash
# Aggiorna pacchetti
apt update && apt upgrade -y

# Installa Python
apt install python3 python3-venv python3-pip -y

# Installa Git
apt install git -y

# Installa Nginx (reverse proxy)
apt install nginx -y

# Clona il repository
cd /var/www
git clone <repository-url> tremare-pub
cd tremare-pub

# Crea virtual environment
python3 -m venv venv
source venv/bin/activate

# Installa dipendenze
pip install -r requirements.txt
pip install gunicorn
```

#### 2.5 Configura Gunicorn
```bash
# Crea file di configurazione
nano /etc/systemd/system/tremare.service
```

Incolla:
```ini
[Unit]
Description=Tremare Pub Flask App
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/tremare-pub
Environment="PATH=/var/www/tremare-pub/venv/bin"
ExecStart=/var/www/tremare-pub/venv/bin/gunicorn -w 4 -b 127.0.0.1:5000 app:app

[Install]
WantedBy=multi-user.target
```

Salva (Ctrl+X, Y, Enter)

```bash
# Abilita servizio
systemctl start tremare
systemctl enable tremare
systemctl status tremare
```

#### 2.6 Configura Nginx
```bash
nano /etc/nginx/sites-available/tremare
```

Incolla:
```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Salva.

```bash
# Abilita sito
ln -s /etc/nginx/sites-available/tremare /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx
```

#### 2.7 SSL con Let's Encrypt (HTTPS)
```bash
apt install certbot python3-certbot-nginx -y
certbot --nginx -d your-domain.com -d www.your-domain.com
```

**URL**: `https://your-domain.com`

### Opzione 3: AWS (Più enterprise)

#### 3.1 Opzioni su AWS
- **Elastic Beanstalk** (semplice, managed)
- **EC2** (più controllo)
- **Lambda** (serverless, billing per uso)

Consigliato: **Elastic Beanstalk**

```bash
# Installa EB CLI
pip install awsebcli

# Crea applicazione
eb init -p python-3.11 tremare-pub --region eu-west-1

# Deploy
eb create tremare-prod
eb open
```

---

## 🔐 PRODUZIONE CHECKLIST

### Before Launch
- [ ] Aggiorna FLASK_ENV a `production`
- [ ] Imposta SECRET_KEY robusto (secret di 32+ caratteri)
- [ ] Disabilita debug mode (FLASK_DEBUG=False)
- [ ] Configura email service (per future funzionalità)
- [ ] Setup database (se necessario)
- [ ] Configura backups automatici
- [ ] Setup monitoring (uptime, errors)
- [ ] Setup logging centralizzato
- [ ] Security headers configured
- [ ] SSL/HTTPS enabled
- [ ] Rate limiting attivo

### Security Headers (Nginx)
Aggiungi a nginx config:
```nginx
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Referrer-Policy "no-referrer-when-downgrade" always;
```

### Monitoring Tools Consigliati
- **Uptime**: UptimeRobot (free tier)
- **Errors**: Sentry.io (free tier)
- **Logs**: Loggly, Papertrail
- **Analytics**: Google Analytics 4

---

## 📧 EMAIL CONFIGURATION (Future)

### Setup SendGrid
```bash
pip install sendgrid python-dotenv
```

Aggiungi a app.py:
```python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(to_email, subject, html_content):
    message = Mail(
        from_email='noreply@tremarepub.it',
        to_emails=to_email,
        subject=subject,
        html_content=html_content
    )
    sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
    response = sg.send(message)
    return response
```

### Setup Brevo (ex Sendinblue)
```bash
pip install mailin
```

---

## 🐳 DEPLOYMENT CON DOCKER (Advanced)

### Crea Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

### Crea .dockerignore
```
.git
.gitignore
__pycache__
.venv
venv
*.pyc
.DS_Store
```

### Build e Run
```bash
# Build
docker build -t tremare-pub .

# Run locale
docker run -p 5000:5000 tremare-pub

# Push a Docker Hub
docker tag tremare-pub:latest username/tremare-pub:latest
docker push username/tremare-pub:latest
```

---

## 📊 MONITORING & MAINTENANCE

### Log Rotation (Linux)
```bash
nano /etc/logrotate.d/tremare
```

```
/var/www/tremare-pub/logs/*.log {
    daily
    rotate 14
    compress
    delaycompress
    notifempty
    create 0640 www-data www-data
}
```

### Health Check Endpoint (Future)
```python
@app.route('/health')
def health():
    return {'status': 'ok', 'timestamp': datetime.now()}
```

### Backup Database (Future)
```bash
# Cron job (run daily at 2 AM)
0 2 * * * pg_dump tremare_db > /backups/tremare_$(date +\%Y\%m\%d).sql
```

---

## 🔧 TROUBLESHOOTING

### Flask non si avvia
```bash
# Verifica Python
python --version

# Verifica Flask
pip list | grep Flask

# Reinstalla dipendenze
pip install --force-reinstall -r requirements.txt
```

### Errore: "Address already in use"
```bash
# Cambia porta
python app.py --port 5001

# Oppure kill il processo che occupa 5000
# Windows: netstat -ano | findstr :5000
# Linux: lsof -i :5000
```

### Database locked
```bash
# Se usi SQLite, elimina file .db
rm tremare.db
```

### WhatsApp link non funziona
Verifica che il numero sia nel formato corretto: `+39XXXXXXXXX` (senza spazi/caratteri speciali)

---

## 🎓 NEXT STEPS

1. **Customizzazione**:
   - Aggiorna menù con veri items
   - Aggiungi immagini professionali
   - Personalizza testi

2. **Database** (quando pronto):
   - Installa PostgreSQL
   - Setup Flask-SQLAlchemy
   - Crea models (Reservations, Orders)

3. **Payment**:
   - Integra Stripe o Satispay
   - Setup webhook handlers

4. **Admin Panel**:
   - Crea dashboard
   - Menu management
   - Order management

5. **Mobile App** (future):
   - React Native o Flutter app
   - Push notifications
   - Order tracking

---

## 📞 SUPPORT

Per problemi di deployment, contatta il web developer o apri una issue su GitHub.

---

**Last Updated**: June 15, 2024
**Version**: 1.0
