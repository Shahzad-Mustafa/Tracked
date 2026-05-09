from .base import *
import dj_database_url

DEBUG = False

# PostgreSQL if DATABASE_URL is set, otherwise SQLite (fine for portfolio)
_db_url = os.environ.get('DATABASE_URL')
if _db_url:
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600, conn_health_checks=True)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

EMAIL_HOST_USER     = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')

if EMAIL_HOST_USER and EMAIL_HOST_PASSWORD:
    EMAIL_BACKEND  = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST     = 'smtp.gmail.com'
    EMAIL_PORT     = 587
    EMAIL_USE_TLS  = True
else:
    EMAIL_BACKEND  = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = os.environ.get(
    'DEFAULT_FROM_EMAIL', 'Shahzad Ali <Shahzadmustafa755@gmail.com>'
)

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',')
