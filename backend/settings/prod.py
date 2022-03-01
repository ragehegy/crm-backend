try:
    from . import *
except ImportError:
    pass

DEBUG = False

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
