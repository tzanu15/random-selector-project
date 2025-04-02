import os
from pathlib import Path
from datetime import timedelta

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key used for cryptographic signing
SECRET_KEY = 'your-secret-key'  # Replace with a real secret key in productionpip

# Toggle for debug mode (should be False in production)
DEBUG = True

# List of allowed hosts for this server
ALLOWED_HOSTS = []

# Applications registered in this Django project
INSTALLED_APPS = [
    'django.contrib.admin',        # Admin panel
    'django.contrib.auth',         # Authentication system
    'django.contrib.contenttypes', # Content types framework
    'django.contrib.sessions',     # Session management
    'django.contrib.messages',     # Messaging framework
    'django.contrib.staticfiles',  # Static files management

    'rest_framework',              # Django REST Framework
    'rest_framework_simplejwt',    # JWT authentication

    # Your apps
    'apps.accounts',
    'apps.teams',
    'apps.wheel',
    'apps.core',
]

# Middleware classes used by Django for processing requests/responses
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'config.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add your templates folders here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application entry point
WSGI_APPLICATION = 'config.wsgi.application'

# Database configuration using SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',       # Use SQLite
        'NAME': BASE_DIR / 'db.sqlite3',              # Database file location
    }
}

# Password validation rules
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Default language code
LANGUAGE_CODE = 'en-us'

# Time zone setting
TIME_ZONE = 'UTC'

# Enable internationalization
USE_I18N = True

# Enable timezone-aware datetimes
USE_TZ = True

# Static files URL (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST framework global configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# JWT settings for token expiration and behavior
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  # Token expires after 1 hour
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),     # Refresh token expires after 1 day
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}
