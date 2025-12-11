
# 📚 SmartLib – Library Management System

SmartLib is a web-based library management system  
It allows the user to:

- Manage books (add, edit, delete, list)
- Manage members
- Borrow and return books
- Purchase books
- Submit ratings and feedback
- View transactions and history through the Django admin and the system 

This README explains how to **run the system in the same way it was developed**, using Anaconda and the `library_env` environment.

---

## ✅ Requirements

To run this SmartLib, you need:

- **Anaconda** (or Python 3.10+)
- **MongoDB** (local installation)
- **MongoDB Compass** (optional, for visual database access)
- **Git** (optional, for cloning the repository)

The project was developed using:

- Anaconda environment: `library_env`
- Django
- Djongo + PyMongo

All required packages were installed inside `library_env`.

---

## 📥 Getting the Project

You can obtain the project from GitHub:

**Repository link:**  
https://github.com/abraralawadhi-debug/it7405-project-an

Two options:

1. **Download ZIP**
   - Click the green **Code** button → **Download ZIP**
   - Extract the ZIP file (for example to your Desktop)

2. **Or clone using Git**
   ```bash
   git clone https://github.com/abraralawadhi-debug/it7405-project-an.git
   cd it7405-project-an


---
## 🔌 Running the SmartLib System (Full Command Guide)

To run the SmartLib system exactly as it was developed, follow these steps:

1️⃣ Install Anaconda & Create the Virtual Environment

Step A — Open Anaconda Prompt

Step B — Create the environment (only once):

`conda create -n library_env python=3.10 -y`

Step C — Activate the environment:
conda activate library_env

2️⃣ Install Required Python Packages

`pip install -r requirements.txt`

Inside your project folder, run:

`pip install django`

`pip install djongo`

`pip install pymongo`

`pip install dnspython`


These are the exact packages used during development.

3️⃣ Set Up MongoDB

Install MongoDB Community Server

Download from: https://www.mongodb.com/try/download/community

Start MongoDB service

On Windows, it usually starts automatically.

No configuration needed

Your `settings.py` already contains:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'library_db',
    }
}
```
---

SmartLib will automatically create collections when the system runs.

4️⃣ Run the Development Server

Step 1 — Activate the environment

`conda activate library_env`

Step 2 — Navigate to the project folder

Example:

cd "C:\Users\abrar\OneDrive\Desktop\it7405-project-an"

Step 3 — Run the server

`python manage.py runserver`

The system will now be available at:

✔ Main Website:

http://127.0.0.1:8000/

✔ Admin Panel:

http://127.0.0.1:8000/admin/

To create a Django Admin login:

`python manage.py createsuperuser`

🎉 Your SmartLib Setup Is Complete!



