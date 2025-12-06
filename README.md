
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

To run this project, you need:

- **Anaconda** (or Python 3.10+)
- **MongoDB** (local installation)
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

1. Install Anaconda & Create the Virtual Environment
Step A — Open Anaconda Prompt
Step B — Create the environment (only once): 

`conda create -n library_env python=3.10`

Step C — Activate the environment:

`conda activate library_env`

2. Install Required Python Packages

Inside your project folder, run:

`pip install django`

`pip install djongo`

`pip install pymongo`

`pip install dnspython`



These are the exact packages used during development.

 3. Set Up MongoDB

Install MongoDB Community Server

Start the MongoDB service

On Windows, it usually starts automatically

No extra configuration needed

Your settings.py already includes:

`DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'smartlib',
    }
}`

 4. Apply Django Migrations

Although the project uses MongoDB, Django still requires migrations.

Run:

`python manage.py makemigrations`

`python manage.py migrate`


 5. Create a Superuser (optional but recommended)
`python manage.py createsuperuser`


This will create login access for the Django Admin Panel.

 6. Run the Development Server

Start the server:

`python manage.py runserver`


The system will now be available at:

http://127.0.0.1:8000/

Admin panel:

http://127.0.0.1:8000/admin/



