# 📡 wifi-drop

Upload files from your phone to your laptop — directly, over Wi-Fi — with no internet, no app, and full privacy.

---

## 📦 About the Project

**wifi-drop** lets you quickly send photos and files from your phone to your laptop over a local Wi-Fi network or mobile hotspot.  
No cables. No apps. No internet required.

It works entirely in the browser and stores files directly on your computer.

---

## 🚀 Features

- ✅ Works offline (Wi-Fi or mobile hotspot)
- ✅ No app or installation needed on phone
- ✅ Mobile-friendly UI
- ✅ Skips files that already exist (checked before upload begins)
- ✅ Shows upload progress per file
- ✅ Up to 3 files upload in parallel automatically
- ✅ Background uploads — safe to lock your screen or switch apps (Android Chrome)
- ✅ HTTPS — encrypted transfers, required for background upload support
- ✅ Falls back to standard upload on browsers without Background Fetch (iOS Safari, Firefox)

---

## 🛠️ How to Set Up

### 📁 Step 1: Create a Python Virtual Environment (optional but recommended)

```
mkdir -p ~/envs
python3 -m venv ~/envs/env_python_wifi_drop
source ~/envs/env_python_wifi_drop/bin/activate
```

### 📦 Step 2: Install Dependencies

```
pip install -r requirements.txt
```

### 🚀 Step 3: Start the Server

```
python3 server.py
```

You should see a message like:

```
🚀 Server running at: https://192.168.1.42:8000
📁 Uploads saved to: /Users/you/wifi-drop/Uploads
⚠️  First visit: tap 'Advanced' → 'Proceed' to accept the self-signed cert
```

A self-signed TLS certificate is generated automatically in `certs/` on first run.

### 📱 Step 4: Open That Link From Your Phone

Connect your laptop and phone to the same Wi-Fi or mobile hotspot.  
On your phone, open Chrome (or any browser) and visit the printed `https://` link.

**First visit only:** the browser will show a certificate warning because the cert is self-signed.
- **Android Chrome:** tap Advanced → Proceed to [IP] (unsafe)
- **iOS Safari:** tap Show Details → visit this website

After accepting once, uploads work normally — including in the background.

💡 **Tip: Use Mobile Hotspot Without Internet**  
You don't need internet. Just enable hotspot on your phone, connect your laptop to it, and upload directly — offline and private. No mobile data is used.

---

## 📁 Folder Structure

```
wifi-drop/
├── server.py               # Entry point — FastAPI app, routes, HTTPS startup
├── config.py               # Constants: UPLOAD_DIR, chunk size, cert paths
├── upload_handler.py       # Upload logic (async writes) and duplicate check
├── middleware.py           # Request timing and stats middleware
├── context.py              # Per-request UUID via contextvars
├── stats.py                # Upload stats tracking (load/save/print)
├── utils.py                # Local IP detection, TLS cert generation
├── static/
│   ├── index.html          # Upload UI (Background Fetch + XHR fallback)
│   └── sw.js               # Service Worker for background upload notifications
├── certs/                  # Auto-generated TLS cert (gitignored)
├── Uploads/                # Where uploaded files are saved (gitignored)
├── upload_stats.json       # Persistent stats (generated at runtime)
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Requirements

- Python 3.8+
- Works on Linux, macOS, or Windows
- **Android Chrome** for full background upload support
- Any modern browser for standard uploads (iOS Safari, Firefox, etc.)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🚀 What Can Be Improved / Future Ideas

- ✅ Upload files in parallel for speed
- ✅ Background uploads using Service Workers + Background Fetch API
- ✅ Auto-detect and display the correct IP address
- ✅ Skip files that already exist
- Add file size limit to prevent huge uploads
- Show list of already-uploaded files on the webpage
- Add drag-and-drop file support (improves mobile UX)
- 🔒 Add password or PIN protection for basic security
- Add upload cancellation or retry mechanisms
- Zip files before uploading to save bandwidth
- Let user choose upload destination folder via the webpage (with security)
- Turn this into a full Progressive Web App (PWA) with install prompt and offline manifest
- Package as a desktop app (.desktop for Linux, etc.)

---

### 🤝 Contributing

Pull requests are welcome!  
If you've got an idea for a feature, bug fix, or improvement — open an issue or submit a PR.

### 💬 Credits & Inspiration

Inspired by the need to move files quickly without third-party apps, cables, or internet.
