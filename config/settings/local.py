from .development import *

DEBUG = True
# config/settings/base.py

LOGIN_REDIRECT_URL = "/api/accounts/users/"
LOGOUT_REDIRECT_URL = "/api-auth/login/"