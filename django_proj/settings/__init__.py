try:
    from .base import *
except ImportError:
    pass

try:
    from .dev import *
except ImportError:
    pass


# from django_proj.settings import test_settings