"""
Django settings for phones_mitht project.
Generated by 'django-admin startproject' using Django 1.8.3.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
from os.path import abspath, basename, dirname, join, normpath
import djcelery
import sys

SITE_ID = 1
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_PATH = os.path.abspath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4%u+lvugiuaoy7_p&$l#r8asi)5jp@di&$&h0%=g70t6kyv1%9'

# SECURITY WARNING: don't run with debug turned on in production!
if socket.gethostname() == 'webhost3':
    DEBUG = TEMPLATE_DEBUG = False
else:
    DEBUG = TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['webhost3', '127.0.0.1']

# Application definition
INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'phones',
    'ckeditor',
    'mptt',
    'django_mptt_admin',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'haystack',
    'fontawesome',
    'django.forms',
    'sorl.thumbnail',
    'publications',
    'endless_pagination',
    'celery',
    'celery_haystack',
    'fixture_magic',
)

MIDDLEWARE_CLASSES = (

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

)

ROOT_URLCONF = 'phones_mitht.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            normpath(join(BASE_DIR, 'phones/templates')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.core.context_processors.debug",
                "django.core.context_processors.i18n",
                "django.core.context_processors.static",
                "django.core.context_processors.media",
                "django.core.context_processors.request",
            ],
        },
    },
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

WSGI_APPLICATION = 'phones_mitht.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
if socket.gethostname() == 'webhost3':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'phonebook',
            'USER': 'phone',
            'PASSWORD': 'ReNsKtDcThUtQ1988',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = normpath(join(BASE_DIR, 'static', 'collected'))

STATICFILES_DIRS = (
    normpath(join(BASE_DIR, 'static')),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'phones',  'images')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'phones',  'templates'),
)

CKEDITOR_UPLOAD_PATH = (
    os.path.join(BASE_DIR,  'uploads'),
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://178.62.255.252:9266/',
        'INDEX_NAME': 'haystack',
    },
}
# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Справочник МИТХТ',
    'HEADER_DATE_FORMAT': 'l, j E Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
        'phones': 'icon-book',
        'socialaccount': 'icon-leaf',
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
    },

   # 'MENU_EXCLUDE': ('socialaccount','sites'),
   # 'MENU': (
   #      {'app': 'phones', 'label':'Телефоны','models': ('person', '-', 'unit', 'position', 'degree', 'sciencerank', 'workhours', '-', 'address', 'city', 'street', 'building', 'campus', 'office', 'areacode', 'postcode', 'prefix', 'phone',)},
   # ),

    # misc
    # 'LIST_PER_PAGE': 15
}

FONTAWESOME_CSS_URL = '//maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css'
FONTAWESOME_PREFIX = 'fa'


SOCIALACCOUNT_PROVIDERS = \
    {'google':
        {'SCOPE': ['profile', 'email'],
          'AUTH_PARAMS': {'access_type': 'online'}}}

THUMBNAIL_PREFIX = 'images/cache/'
HAYSTACK_SIGNAL_PROCESSOR = 'celery_haystack.signals.CelerySignalProcessor'