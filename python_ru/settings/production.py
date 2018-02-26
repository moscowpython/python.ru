from __future__ import absolute_import, unicode_literals

from .base import *

# Setting the development status:

DEBUG = config('DEBUG', default=False, cast=bool)

DATABASES = {
    'default': {
        'ENGINE': config('DATABASES_ENGINE'),
        'NAME': config('DATABASES_NAME'),
        'USER': config('POSTGRES_API_USER'),
        'PASSWORD': config('POSTGRES_API_PASSWORD'),
        'HOST': config('POSTGRES_API_HOST'),
        'PORT': config('POSTGRES_API_PORT', cast=int, default=5432),
    }
}
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
