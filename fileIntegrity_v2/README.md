# 🛡️ File Integrity Monitoring System – Agent App

This project is part of my internship work titled **File Integrity Monitoring System** @InfinitumIT. The system is composed of three main components:

1. 🌐 Web App  
2. ⚙️ Backend App  
3. 🖥️ Agent App *(this repository)*

---

## 📌 Overview

The **Agent App** is responsible for monitoring directories specified by the user via the Web App. It detects and reports the following file system events:

- 🆕 File creations  
- ✏️ File modifications  
- ❌ File deletions  

---

## ⚙️ Technologies Used

- **Python 3.13**
- **[Watchdog](https://pypi.org/project/watchdog/)** – for directory monitoring
- **[Flask](https://flask.palletsprojects.com/)** – for running the internal server
- **[PyInstaller](https://pyinstaller.org/)** – for building the agent into a single executable (`--onefile`)

---

## 🚀 Features

- Real-time directory monitoring
- Event reporting (create/modify/delete)
- Token-based activation
- Web-based directory management
- Simple CLI-based setup

---

## 📦 How to Run the Agent

### ✅ Prerequisites

- Ensure the **Backend App** is running and accessible
- Python 3.13 installed (or use the compiled onefile executable)

### ▶️ Steps

1. Go to the Web App and log in to your account.
2. Open your terminal and navigate to the agent directory:
   ```bash
   cd /fileIntegrity_v2
3. Run the agent:

    ```bash
    python agent.py
4. Enter your activation token when prompted (can be claimed from the Web App).

5. Add the directories you want to monitor via the Web App interface.

6. The agent will now begin monitoring and reporting file events! ✅ 

---

# 📝 Notes
- The agent should be run on the system you want to monitor.

- Ensure network access between the agent and the backend API.

# 👨‍💻 Author
- Nisa Dost
- Intern @ InfinitumIT
- Project: FileIntegrity Monitoring System