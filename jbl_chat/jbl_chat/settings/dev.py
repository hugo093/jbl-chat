from .base import *

DEBUG = True

WSGI_APPLICATION = 'jbl_chat.wsgi.dev.application'
ASGI_APPLICATION = "jbl_chat.asgi.dev.application"
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE = MIDDLEWARE + ['debug_toolbar.middleware.DebugToolbarMiddleware']

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]  # nosec

# Debug toolbar config
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel'
]

def custom_show_toolbar(request):
    return DEBUG


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': 'jbl_chat.settings.dev.custom_show_toolbar',
    'ENABLE_STACKTRACES': True,
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}