from .base import *

DEBUG = False
WSGI_APPLICATION = 'jbl_chat.wsgi.application.production'
ASGI_APPLICATION = 'jbl_chat.asgi.application.production'
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", 'jbl_chat']  # nosec

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "jbl_chat",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "postgres-jbl-chat",
        "PORT": ""
    }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}