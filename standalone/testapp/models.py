from django.db import models

# Construct Django models like normal. When you're done, you can use syncdb, or
# a migration management app (which I recommend) like South to manage your
# database.
#
# With South, if you change your models, run:
#
#     python manage.py schemamigration <appname> --auto
#     python manage.py migrate <appname>
#
class TestModel (models.Model):
    myfield = models.TextField()
    myinteger = models.IntegerField(null=True)
