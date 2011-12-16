from django.db import models

# Construct Django models like normal. When you're done, you can use syncdb, or
# a migration management app (which I recommend) like South to manage your
# database.
class TestModel (models.Model):
    myfield = models.TextField()
    myinteger = models.IntegerField(null=True)
