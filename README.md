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
- ✅ Skips files that already exist  
- ✅ Shows upload progress and time per file

---

## 🛠️ How to Set Up

Here’s how to set up and run `wifi-drop` locally:

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

Server started: http://192.168.1.42:8000

### 📱 Step 4: Open That Link From Your Phone

Connect your laptop and phone to the same Wi-Fi or mobile hotspot.
On your phone, open any browser (Chrome, Safari, etc.)
Visit the printed link (e.g., http://192.168.1.42:8000)
Select files → Upload → Done ✅

💡 Tip: Use Mobile Hotspot Without Internet
You don’t need internet. Just:
Enable hotspot on your phone.
Connect your laptop to it.
Upload directly — offline and private.
✅ No mobile data is used.


### 📁 Folder Structure
```
wifi-drop/
├── server.py              # Python server (FastAPI or HTTP handler)
├── static/
│   └── index.html         # Upload page UI
├── uploads/               # Folder where uploaded files are stored
├── requirements.txt       # Python dependencies
├── .gitignore
└── README.md
```

### 👨‍💻 Requirements
- Python 3.7+
- Works on Linux, macOS, or Windows
- A modern browser on your phone (no app needed)

### 📄 License
This project is licensed under the MIT License.

## 🚀 What Can Be Improved / Future Ideas

- ✅ Add file size limit to prevent huge uploads  
- ✅ Show list of uploaded files directly on the webpage  
- ✅ Add drag-and-drop file support (improves mobile UX)  
- 🔒 Add password or PIN protection for basic security  
- Package as a desktop app (.desktop for Linux, etc.)  
- Add full authentication (login system)  
- Improve upload progress bar and per-file timing  
- ⚡ Upload files in parallel for speed (more accurate time estimates needed)  
- 📝 Show list of uploaded filenames on the UI  
- 🎨 Enhance UI/UX on mobile with more responsive design  
- 💾 Let user choose upload destination folder via the webpage (with security)  
- Turn this into a Progressive Web App (PWA) for offline use and installation  
- Add upload cancellation or retry mechanisms  
- Zip files before uploading to save bandwidth  
- Auto-detect and display the correct IP address to connect easily  
- Implement queuing and resuming uploads in offline mode using Service Workers or similar tech  


### 🤝 Contributing
Pull requests are welcome!
If you’ve got an idea for a feature, bug fix, or improvement — open an issue or submit a PR.

### 💬 Credits & Inspiration
Inspired by the need to move files quickly without third-party apps, cables, or internet.
