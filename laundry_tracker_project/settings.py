from pathlib import Path
from .configs import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-lps2fp1=#^fgw(-3ju7&hy%olws_e049tj1i#u$)wq7=tk8-ad"
DEBUG = True
ALLOWED_HOSTS = ['https://django-loundary-tracker-project.onrender.com', '127.0.0.1', 'localhost']
CSRF_TRUSTED_ORIGINS = ['https://django-loundary-tracker-project.onrender.com', '127.0.0.1', 'localhost']


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "home",
    "accounts",
    "loading_start",
    "loading_end",
    "unloading_start",
    "unloading_end",
    "packing",
    "nursing_station",
    "task_schedule",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "laundry_tracker_project.urls"

# Configure two template engines:
# 1. DjangoTemplates for the admin and other parts that require it.
# 2. Jinja2 for your application templates, stored in the existing "templates" folder.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # Django admin uses its built-in templates.
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
    {
        "BACKEND": "django.template.backends.jinja2.Jinja2",
        "DIRS": [BASE_DIR / "templates"],  # Use the existing templates directory for Jinja2.
        "APP_DIRS": False,  # Jinja2 doesn't auto-load templates from app directories.
        "OPTIONS": {
            "environment": "laundry_tracker_project.jinja2.environment",
        },
    },
]

WSGI_APPLICATION = "laundry_tracker_project.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
    }
}

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

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = '/accounts/'
