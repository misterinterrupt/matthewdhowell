import os, sys, socket
# Set DEBUG = True if on the production server
if socket.gethostname() == 'matthewdhowell.com':
    DEBUG = False
else:
    DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('matt_admin', 'matthewdhowell@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mattvoid.sqlite3', # Or path to database file if using sqlite3.
        'USER': '', # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}