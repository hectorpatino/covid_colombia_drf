import dj_database_url
import django_heroku
import os
from pathlib import Path

from .base import *

DEBUG = False
ALLOWED_HOSTS = []
ADMINS = (
    ('Hector patiño', 'hectorpatino24@gmail.com'),
)
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

django_heroku.settings(locals())
