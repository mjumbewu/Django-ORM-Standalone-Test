"""
This module is a stripped-down version of the default django settings module
that is created with every django project.  To get one of your own, just run::

    django-admin.py startproject myproject

In the resulting myproject folder will be a settings.py file.  All that we need
to use the ORM is the DATABASES setting and an app for our models.
"""

# To keep things simple, I used an sqlite database.  Fill in the settings for
# your own.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ormtest.db',                   # Or path to database file if using sqlite3.
        'USER': '',                             # Not used with sqlite3.
        'PASSWORD': '',                         # Not used with sqlite3.
        'HOST': '',                             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Create a new app using the `python manage.py startapp <appname>` command.  I
# named my app 'testapp'.  In the app package, all you need are the __init__.py
# and the models.py files.  I also included South for DB management.
INSTALLED_APPS = (
    'testapp',
    'south',
)
