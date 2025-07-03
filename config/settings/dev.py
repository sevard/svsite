from .base import *


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# In case we need it in development environment
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DBNAME'),
#         'HOST': os.getenv('DBHOST', 'localhost'),
#         'USER': os.getenv('DBUSER'),
#         'PASSWORD': os.getenv('DBPASS'),
#         # 'PORT': os.getenv('DBPORT', '5432'),
#     }
# }