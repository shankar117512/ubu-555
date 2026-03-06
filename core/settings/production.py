from .base import *

DEBUG = False

ALLOWED_HOSTS = ["peaceful-youth-production.up.railway.app"]
CSRF_TRUSTED_ORIGINS = ["https://peaceful-youth-production.up.railway.app"]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
