# Django settings for idptest project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

import os
PROJECT_ROOT = os.getcwd()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '%s/idptest.sqlite' % PROJECT_ROOT,                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Backwards-compatibility for Django 1.1:
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = DATABASES['default']['NAME']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'q+0vb%)c7c%&kl&jcca^6n7$3q4ktle9i28t(fd&qh28%l-%58'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware'
)

ROOT_URLCONF = 'idptest.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '%s/templates' % PROJECT_ROOT,
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'saml2idp',
)

LOGIN_REDIRECT_URL = '/idp/sso/post/response/preview/'

# SAML2IDP metadata settings
SAML2IDP_CONFIG = {
    'autosubmit': False,
    'issuer': 'http://127.0.0.1:8000',
    'signing': True,
    'certificate_file': PROJECT_ROOT + '/keys/sample/sample-certificate.pem',
    'private_key_file': PROJECT_ROOT + '/keys/sample/sample-private-key.pem',
}

demoSpConfig = {
    'acs_url': 'http://127.0.0.1:9000/sp/acs/',
    'processor': 'saml2idp.demo.Processor',
    'links': [ # a list of (resource, pattern) tuples, or a {resource: pattern} dict
        #NOTE: This should still work, due to the "simple" 'login_init' URL in urls.py:
        #TEST BY BROWSING TO: http://127.0.0.1:8000/sp/test/
        ('deeplink', 'http://127.0.0.1:9000/sp/%s/'),
        # The following are "new" deeplink mappings that let you specify more than one capture group:
        # This is equivalent to the above, using the 'new' deeplink mapping:
        #TEST BY BROWSING TO: http://127.0.0.1:8000/sp/test/
        (r'deeplink/(?P<target>\w+)', 'http://127.0.0.1:9000/sp/%(target)s/'),
        # Using two capture groups:
        #TEST BY BROWSING TO: http://127.0.0.1:8000/sp/test/
        (r'deeplink/(?P<target>\w+)/(?P<page>\w+)', 'http://127.0.0.1:9000/%(target)s/%(page)s/'),
        # Deeplink to a resource that requires query parameters:
        #NOTE: In the pattern, always use %(variable)s, because the captured
        # parameters will always be in unicode.
        #TEST BY BROWSING TO: http://127.0.0.1:8000/sp/test/123/
        (r'deeplink/(?P<target>\w+)/(?P<page>\w+)/(?P<param>\d+)',
            'http://127.0.0.1:9000/%(target)s/%(page)s/?param=%(param)s'),
    ],
}
attrSpConfig = {
    'acs_url': 'http://127.0.0.1:9000/sp/acs/',
    'processor': 'saml2idp.demo.AttributeProcessor',
    'links': {
        'attr': 'http://127.0.0.1:9000/sp/%s/',
    },
}
SAML2IDP_REMOTES = {
    # Group of SP CONFIGs.
    # friendlyname: SP config
    'attr_demo': attrSpConfig,
    'demo': demoSpConfig,
}

# Setup logging.
import logging
logging.basicConfig(filename=PROJECT_ROOT + '/saml2idp.log', format='%(asctime)s: %(message)s', level=logging.DEBUG)
logging.info('Logging setup.')
