# -*- coding: utf-8 -*-

import dj_database_url

from unipath import Path

PROJECT_DIR = Path(__file__).parent

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config(
        default="sqlite:///" + PROJECT_DIR.child('databases.db'))
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = PROJECT_DIR.child('public')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR.child('static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'mpf7l$q5tcw@+!81jkow-xong6wt6xm-(wh!9x_pc_9z6+2z^i'

# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',

    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'openspace.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'openspace.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR.child('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'django.contrib.admin',

    'south',
    'social_auth',

    'openspace.core',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Django Grappelli
GRAPPELLI_ADMIN_TITLE = "FLISOL Openspace"

import os
TINY_MCE_FILES = [
    os.path.join(STATIC_URL, 'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js'),
    os.path.join(STATIC_URL, 'js/tinymce_setup/tinymce_setup.js'),
]

# Django Social Auth
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.contrib.github.GithubBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    'social_auth.backends.OpenIDBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Tokens
FACEBOOK_APP_ID = '240496666095028'
FACEBOOK_API_SECRET = '74fbb791ff5a8d2fceee88057b9d3c34'
GOOGLE_OAUTH2_CLIENT_ID = '681640174227.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'cU7uYErp7OkBTkS4pBBJuBmj'
GITHUB_APP_ID = 'ba1e47649365205359a8'
GITHUB_API_SECRET = 'a0f3ad5e643d76eb60da8a0518e8f91dc388f74b'
YAHOO_CONSUMER_KEY = 'dj0yJmk9M1NmSmdvWVNpdzJFJmQ9WVdrOVJVZHNPV0ZHTkdNbWNHbzlNVE00TnpVeU5EazJNZy0tJnM9Y29uc3VtZXJzZWNyZXQmeD1jNw--'
YAHOO_CONSUMER_SECRET = '6bb5f943f5bca2717d3bf792c2e48cff047596b8'

# Linkedin Backend
LINKEDIN_SCOPE = ['r_basicprofile', 'r_emailaddress', ]
LINKEDIN_EXTRA_FIELD_SELECTORS = ['email-address', 'headline']
LINKEDIN_EXTRA_DATA = [('id', 'id'),
                       ('first-name', 'first_name'),
                       ('last-name', 'last_name'),
                       ('email-address', 'email_address'),
                       ('headline', 'headline'), ]

# Facebook Backend
FACEBOOK_EXTENDED_PERMISSIONS = ['email']
FACEBOOK_AUTH_EXTRA_ARGUMENTS = {'locale': 'pt_BR'}

# Qual página redirecionar após o login
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

# Qual página redirecionar após o logout
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/'

# Qual página redirecionar quando ocorrer algum erro
# na autenticação da conta.
SOCIAL_AUTH_BACKEND_ERROR_URL = '/login/error/'

# Define quais campos não devem ser atualizados quando
# efetuar uma nova autenticação
SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email', ]
