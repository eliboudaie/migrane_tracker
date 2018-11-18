from django.db import models
from django.contrib.auth.models import User


class PrecedingSymptom(models.Model):
    symptom = models.CharField(max_length=100)

    def __str__(self):
        return self.symptom


class Trigger(models.Model):
    trigger = models.CharField(max_length=100)

    def __str__(self):
        return self.trigger



relief_choices = (
    ("COMPLETE", "Complete"),
    ("MODERATE", "Moderate"),
    ("NONE", "None"),
)

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time =  models.DateTimeField()
    intensity = models.PositiveSmallIntegerField()
    preceding_symptoms = models.ManyToManyField(PrecedingSymptom)
    triggers = models.ManyToManyField(Trigger)
    # TODO: Add Medication & Dosage
    relief = models.CharField(max_length=20, choices=relief_choices)
    notes = models.TextField(blank=True)
    def __str__(self):
        return "Record For: "+self.user.username+" "+str(self.start_time)
