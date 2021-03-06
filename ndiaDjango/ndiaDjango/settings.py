"""
Django settings for ndiaDjango project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import logging
logger = logging.getLogger(__name__)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-s-rbo$hlevlh0f2h5+t_z@tg5v=w%er0gwm2p%h8qz%i!5wa%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'communityAssets',
	'tastypie',
	'leaflet',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ndiaDjango.urls'

WSGI_APPLICATION = 'ndiaDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

def databases():

    # Database config on Heroku is simple
    if 'HEROKU' in os.environ and os.environ['HEROKU']:
        import dj_database_url
        return {
            'default': dj_database_url.config() 
        }
 
    try:
        from ndiaDjango import config
    except ImportError:
        config = None
   
    # Note whether configuration was provided or not
    configed = bool(config) or 'DATABASE_URL' in os.environ

    # Set values with provided configuration or default
    config = config if config else object()
    user = getattr(config, 'user', '')
    password = getattr(config, 'password', '')
    host = os.environ.get('DATABASE_URL', getattr(config, 'host', ''))
    port = getattr(config, 'port', '')
    if configed:
        engine = 'django.db.backends.postgresql_psycopg2'
        name_of_database = getattr(config, 'name_of_database', 'ndia')
        logger.info('Using PostgreSQL Database')
    else:
        engine = 'django.db.backends.sqlite3'
        name_of_database = 'ndia.db'
        logger.info('Using SQLite Database')

    return {
        'default': {
            'ENGINE': engine,
            'NAME': name_of_database,
            'USER': user,
            'PASSWORD': password,
            'HOST': host,
            'PORT': port,
        }
    }


DATABASES = databases()

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'



USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

#the leaflet map configuration
LEAFLET_CONFIG = {
	'DEFAULT_CENTER' : (44.9833, -93.2677),
	'DEFAULT_ZOOM' : 12,
	'MIN_ZOOM' : 9,
	'MAX_ZOOM' : 20,
	}
	
