"""
Django settings for peervotes project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
import dj_database_url
from decouple import config,Csv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

MODE=config("MODE", default="dev")
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'apps.users',
    'apps.api',
     'bootstrap4',
    'crispy_forms',
    'cloudinary',
    'cloudinary_storage',
     
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'peervotes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'peervotes.wsgi.application'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if config('MODE') == "dev":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': '',
        }

    }
# production
else:
    DATABASES = {
        'default': dj_database_url.config(
            default=config('DATABASE_URL')
        )
    }

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


cloudinary.config(
    cloud_name = 'hs8k1napd',
    api_key = '711616426271462',
    api_secret = 'jSwVe26AvQnapdwGEBcFABvfxYA',
)

CLOUDINARY_STORAGE = {
'CLOUD_NAME':'hs8k1napd',
'API_SECRET':'jSwVe26AvQnapdwGEBcFABvfxYA',
'API_KEY':'711616426271462',
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = os.path.join(BASE_DIR, 'staticfiles'),


MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


EMAIL_HOST = "localhost"
EMAIL_PORT = 1025


#SMTP_hostname: smtp.mailgun.org
#Port: 587 (recommended)
#Username: postmaster@sandboxdb3fd0f23b184ef5851a6b59c88a98c9.mailgun.org
#Default password: 4af23f7d7750a14fe34272b4cc93b9c6-6e0fd3a4-915f0a3b

#EMAIL_HOST = "smtp.mailgun.org"
#EMAIL_PORT = 587
#EMAIL_HOST_USER = config("EMAIL_HOST_USER")
#EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
#EMAIL_USE_TLS = True


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
