# -*- coding: utf-8 -*-
"""Django development settings."""
from nenga.core.settings.base import *  # noqa


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ENVIRONMENT = os.path.basename(__file__).split('.py')[0]
ALLOWED_HOSTS = []

INSTALLED_APPS += (

)

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

try:
    from nenga.core.settings.local_settings import *  # noqa
except ImportError:
    pass
