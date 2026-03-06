from .base import *

DEBUG = True
ALLOWED_HOSTS = ["cooperative-enjoyment-staging.up.railway.app", "https://cooperative-enjoyment-staging.up.railway.app"]
CSRF_TRUSTED_ORIGINS = ["https://cooperative-enjoyment-staging.up.railway.app"]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
