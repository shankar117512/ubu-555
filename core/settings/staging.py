from .base import *

DEBUG = False
ALLOWED_HOSTS = ["cooperative-enjoyment-staging.up.railway.app", "https://cooperative-enjoyment-staging.up.railway.app"]
CSRF_TRUSTED_ORIGINS = ["https://cooperative-enjoyment-staging.up.railway.app"]

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
