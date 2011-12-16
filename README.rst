A simple example of how to use the Django ORM standalone.  To use, just run::

    pip install -r requirements.txt

Edit the settings.py file to match your database settings, then run::

    cd standalone
    python manage.py syncdb
    python manage.py migrate

Finally, run the sample script with::

    python testscript.py

To read a little about what's going on in this script, check out:
http://stackoverflow.com/a/938373/123776
