import dj_database_url
import django_heroku

from .base import *

BASE_DIR = BASE_DIR
INSTALLED_APPS = INSTALLED_APPS
DEBUG = False
ADMINS = (
    ('Hector patiño', 'hectorpatino24@gmail.com'),
)
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

django_heroku.settings(locals())
