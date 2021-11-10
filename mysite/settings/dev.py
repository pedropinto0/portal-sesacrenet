from .base import *

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_xba+^e$dqj*7)_=f(!6-)n9ftbm+l0&(@5zbujwgtji0eq!iz'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
    'django_extensions',
]

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

try:
    from .local import *
except ImportError:
    pass
