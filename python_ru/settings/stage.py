from __future__ import absolute_import, unicode_literals

from .base import *

# Setting the development status:

DEBUG = config('DEBUG', default=True, cast=bool)

DATABASES = {
    'default': {
        'ENGINE': config('DATABASES_ENGINE'),
        'NAME': config('DATABASES_NAME'),
        'USER': config('DATABASES_USER'),
        'PASSWORD': config('DATABASES_PASSWORD'),
        'HOST': config('DATABASES_HOST'),
        'PORT': config('DATABASES_PORT', cast=int, default=5432),
    }
}
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
