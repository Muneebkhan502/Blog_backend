Django Blog Application
A full-featured web application built with Django.
User registration, login, and logout
User profile management with avatar upload
Create, read, update, and delete (CRUD) blog posts
Pagination for post listings
Password reset via email
Class-based and function-based views
Django admin interface
Media file handling
Tech Stack
Backend: Python, Django
Database: SQLite (default) / PostgreSQL (production-ready)
Frontend: HTML, CSS, Bootstrap
Auth: Django's built-in authentication system
Getting Started
Prerequisites
Python 3.8+
pip
Installation
1. Create and activate a virtual environment
 python -m venv venv
venv\Scripts\activate           # Windows
2.Install dependencies
pip install -r requirements.txt
python manage.py migrate
4.Create a superuser (optional, for admin access)
python manage.py createsuperuser
5.Run the development server
python manage.py runserver
Project Structure:
├── blog/               # Main blog app (posts, views, models)
├── users/              # User registration, profile, authentication
├── media/              # Uploaded media files (profile pics, etc.)
├── static/             # Static files (CSS, JS)
├── templates/          # HTML templates
├── db.sqlite3          # SQLite database
└── manage.py


