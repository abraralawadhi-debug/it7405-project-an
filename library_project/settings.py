"""
Django settings for library_project project.
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ----------------- BASIC SETTINGS -----------------
SECRET_KEY = "django-insecure-(1&@@@$c9dx2)l(hc+t$k(s9#v%&x3q$csg()$5^us7_ap28dt"

DEBUG = True

ALLOWED_HOSTS: list[str] = []


# ----------------- INSTALLED APPS -----------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # your app
    "library_app",
]


# ----------------- MIDDLEWARE -----------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "library_project.urls"


# ----------------- TEMPLATES -----------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # look for templates inside library_app/templates
        "DIRS": [BASE_DIR / "library_app" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "library_project.wsgi.application"


# ----------------- DATABASE (Django -> MongoDB via Djongo) -----------------
# This makes Django (admin, auth, sessions, etc.) use MongoDB instead of SQLite.
DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "library_db",                # same DB you see in Compass
        "CLIENT": {
            "host": "mongodb://localhost:27017",
        },
    }
}


# ----------------- SESSIONS (stored in MongoDB through Djongo) -----------------
# Use the database-backed session engine (default),
# so a collection "django_session" will appear in library_db.
SESSION_ENGINE = "django.contrib.sessions.backends.db"


# ----------------- PASSWORD VALIDATION -----------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ----------------- INTERNATIONALIZATION -----------------
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# ----------------- STATIC FILES -----------------
STATIC_URL = "static/"


# ----------------- DEFAULT PRIMARY KEY -----------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ----------------- MONGODB SETTINGS (used by mongo_connection.py) -----------------
# This is used by your custom PyMongo code (get_db()).
MONGO_DB = {
    "URI": "mongodb://localhost:27017",
    "NAME": "library_db",
}
