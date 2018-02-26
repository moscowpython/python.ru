from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = config('DEBUG', default=True, cast=bool)

DATABASES = {
    'default': {
        'ENGINE': config('DATABASES_ENGINE'),
        'NAME': os.path.join(BASE_DIR, config('DATABASES_NAME', cast=str)),
    }
}
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
