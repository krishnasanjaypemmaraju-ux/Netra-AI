# 👁️ NETRA AI — नेत्र
### The Eye That Never Sleeps
> Intelligent Real-Time Crime Detection System using AI Vision

---

## 🔴 Problem
Crores of CCTV cameras exist across India — but they only **record**. They never react. Women get harassed, thefts happen, attacks occur — and by the time police are called, the criminal is already gone.

---

## 💡 Solution
NETRA AI connects to any existing CCTV camera, uses **Google Gemini AI** to analyze live footage every 2 seconds, detects social crimes through behavioral pattern analysis, and instantly **alerts police via WhatsApp** — before the crime completes.

---

## 🚨 Crimes Detected
Theft • Assault • Women Harassment • Rape Attempt • Murder Attempt • Kidnapping • Weapon Detection • Child Danger • Distress • Stalking

---

## 🛠️ Tech Stack
| Component | Technology |
|-----------|-----------|
| Camera | OpenCV |
| AI Vision | Google Gemini 2.0 Flash |
| Backend | Python |
| Alerts | Twilio WhatsApp API |
| Dashboard | HTML + JavaScript |

---

## 📁 Project Structure
```
NETRA_AI/
├── .env            # API Keys
├── camera.py       # Captures webcam frames
├── detector.py     # Gemini AI crime detection
├── alerter.py      # WhatsApp police alerts
├── main.py         # Main detection loop
└── dashboard.html  # Live monitoring dashboard
```

---

## ⚙️ Installation
```bash
pip install opencv-python google-generativeai twilio pillow python-dotenv
```

Create `.env` file:
```
GEMINI_KEY=your_gemini_key
TWILIO_SID=your_twilio_sid
TWILIO_TOKEN=your_twilio_token
WHATSAPP_NUMBER=whatsapp:+91XXXXXXXXXX
```

---

## ▶️ Run
```bash
# Terminal 1
python main.py

# Terminal 2
python -m http.server 8080
```
Open browser → `localhost:8080/dashboard.html`

---

## 🌍 Impact
Works on **any existing CCTV** — zero new hardware needed. Police receive instant WhatsApp alerts with crime type, description, and confidence score.

---

**👁️ NETRA AI — Protecting Every Person. Detecting Every Crime.**
