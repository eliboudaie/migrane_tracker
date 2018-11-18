from django.contrib import admin
from tracker.models import PrecedingSymptom, Entry, Trigger

# Register your models here.
admin.site.register([PrecedingSymptom, Entry, Trigger])