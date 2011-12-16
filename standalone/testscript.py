# First configure Django using the local settings in your settings.py module.
from django.conf import settings
import settings as local

settings.configure(
    DATABASES = local.DATABASES,
    INSTALLED_APPS = local.INSTALLED_APPS
)


# The meat of the script starts here.
from testapp.models import *

print TestModel.objects.count()

model = TestModel.objects.create()
model.myfield = "This is a test"
model.save()

print TestModel.objects.count()
