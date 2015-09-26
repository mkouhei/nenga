# -*- coding: utf-8 -*-
"""Django local test settings."""
from nenga.core.settings.base import *  # noqa

# SECURITY WARNING: keep the secret key used in production secret!
# Don't forget to replace me!
SECRET_KEY = 'secret key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ENVIRONMENT = os.path.basename(__file__).split('.py')[0]
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS += (

)

AUTHENTICATION_BACKENDS = (

)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'TEST_NAME': ':memory:',
    }
}

try:
    from nenga.core.settings.local_settings import *  # noqa
except ImportError:
    pass
