import os
import dj_database_url
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd7nakjrf5v9eeg',
        'USER': 'xtlleetpqpcecn',
        'PASSWORD': 'dcbad2801588037460b90409b3b91605b9b6b926fad5fb8145fd3ec74761b341',
        'HOST': 'ec2-18-235-45-217.compute-1.amazonaws.com',
        'PORT': ''
    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
