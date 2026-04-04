# Kontaktformular E-Mail-Weiterleitung Setup

## ✅ Was wurde erstellt:

### 1. **contact-worker.js** (Cloudflare Worker Backend)
- Empfängt Formular-Daten per POST
- Validiert alle Felder (Name, E-Mail, Kategorie, Nachricht)
- Sendet E-Mail an: **info@masspost.store**
- Nutzt MailChannels API (kostenlos in Cloudflare Workers)

### 2. **contact-form.js** (Frontend JavaScript)
- Fängt Formular-Submit ab
- Sendet Daten an Cloudflare Worker
- Zeigt Erfolgs-/Fehlermeldungen
- Loading-State beim Senden

### 3. **contact.html** (Updated)
- Eingebunden: `contact-form.js`
- Formular-ID: `contactForm`

---

## 🚀 Deployment-Schritte:

### Schritt 1: Cloudflare Worker erstellen

1. **Gehe zu:** https://dash.cloudflare.com/ → Workers & Pages → Create Application
2. **Wähle:** "Create Worker"
3. **Name:** `contact-form-handler` (oder beliebig)
4. **Deploy** klicken
5. **Öffne den Editor** (Quick Edit)
6. **Lösche** den Standard-Code
7. **Kopiere** den gesamten Inhalt von `contact-worker.js` ein
8. **Save and Deploy** klicken

### Schritt 2: Custom Domain für Worker (wichtig!)

1. Im Worker Dashboard → **Triggers** → **Add Custom Domain**
2. **Domain:** `contact.masspost.store`
3. **Add Domain** → Cloudflare erstellt automatisch DNS Record

**Alternative (wenn Subdomain nicht gewünscht):**
- Route Pattern: `masspost.store/api/contact*`
- Dann in `contact-form.js` die URL ändern zu: `https://www.masspost.store/api/contact/submit`

### Schritt 3: MailChannels konfigurieren (E-Mail-Versand)

**MailChannels ist KOSTENLOS für Cloudflare Workers!**

1. **Gehe zu:** Cloudflare Dashboard → Email Routing
2. **Enable Email Routing** für `masspost.store`
3. **Destination Address:** `info@masspost.store` (oder deine echte E-Mail)
4. **Verify** die E-Mail-Adresse

**Wichtig:** Im Worker-Code ist bereits MailChannels API integriert!

### Schritt 4: Frontend-URL Update

In `contact-form.js` (Zeile 30):
```javascript
const response = await fetch('https://contact.masspost.store/submit', {
```

**Anpassen auf deine Worker-URL:**
- Wenn Custom Domain: `https://contact.masspost.store/submit`
- Wenn Route Pattern: `https://www.masspost.store/api/contact/submit`
- Wenn nur Worker-URL: `https://contact-form-handler.DEIN-SUBDOMAIN.workers.dev/submit`

---

## 📧 E-Mail-Format:

**Betreff:** `[MediaMass Kontakt] TikTok Mass Posting - Max Mustermann`

**Inhalt:**
```
Neue Kontaktanfrage von MediaMass Website
==========================================

Von: Max Mustermann
E-Mail: max@example.com
Kategorie: TikTok Mass Posting

Nachricht:
----------
Ich interessiere mich für Ihre Services...

==========================================
Gesendet über: www.masspost.store/contact.html
Zeitstempel: 04.04.2026, 10:57:00
```

**Reply-To:** Kundens E-Mail (direkt antworten möglich!)

---

## 🔒 Sicherheit & Validation:

✅ **CORS Headers** (nur von masspost.store)
✅ **E-Mail Regex Validation**
✅ **Required Field Checks**
✅ **Rate Limiting** (Cloudflare Workers Standard)
✅ **XSS Protection** (Input Sanitization)

---

## 🧪 Testing:

1. **Nach Deployment:**
   - Gehe zu: https://www.masspost.store/contact.html
   - Fülle Formular aus
   - Klicke "Nachricht senden"
   - Warte auf ✅ Erfolgsmeldung

2. **Prüfe E-Mail:**
   - Schaue in **info@masspost.store** Postfach
   - E-Mail sollte innerhalb 1-2 Minuten ankommen

3. **Bei Fehlern:**
   - Cloudflare Dashboard → Workers → contact-form-handler → Logs
   - Zeigt alle Fehler/Requests in Echtzeit

---

## 🎯 Alternative: Formspree (einfacher, aber kostenpflichtig)

Falls Cloudflare Worker zu komplex:

1. **Gehe zu:** https://formspree.io/
2. **Create Free Account**
3. **Neues Formular erstellen** → E-Mail: info@masspost.store
4. **Formspree Endpoint kopieren** (z.B. `https://formspree.io/f/XXXXXX`)
5. In `contact-form.js` Zeile 30 ändern:
   ```javascript
   const response = await fetch('https://formspree.io/f/XXXXXX', {
   ```

**Vorteile:**
- ✅ Kein Backend-Code nötig
- ✅ Sofort funktionsfähig
- ✅ 50 Submissions/Monat GRATIS

**Nachteile:**
- ❌ Begrenzt auf 50/Monat (Free Plan)
- ❌ Formspree Branding in E-Mails

---

## 📝 Nächste Schritte:

1. ✅ Files committed (contact-worker.js, contact-form.js, contact.html)
2. ⏳ **DU MUSST:** Cloudflare Worker deployen (siehe Schritt 1-3 oben)
3. ⏳ **DU MUSST:** Worker-URL in contact-form.js eintragen
4. ⏳ Git commit + push
5. ✅ Formular ist live!

---

## 🆘 Support:

**Brauchst du Hilfe beim Deployment?** Sag Bescheid!
- Ich kann dich Schritt-für-Schritt durch Cloudflare Dashboard führen
- Oder Formspree-Setup machen (einfacher, 2 Minuten)

**Wichtig:** Ohne Worker-Deployment funktioniert das Formular noch nicht richtig (zeigt Fehler).
