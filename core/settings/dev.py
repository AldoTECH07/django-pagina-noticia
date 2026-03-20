from .base import *

SECRET_KEY = 'django-insecure-123456789'
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'news_db',        # O banco que você criou no SQLTools
        'USER': 'postgres',       # Usuário padrão
        'PASSWORD': '123456789',  # Sua senha do Postgres
        'HOST': 'localhost',
        'PORT': '5432',
    }
}