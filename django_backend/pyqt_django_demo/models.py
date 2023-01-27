from django.db import models


# Create your models here.
class Patient(models.Model):
    patient_first_name = models.CharField(max_length=200)
    patient_last_name = models.CharField(max_length=200)
    patient_birthdate = models.DateField()
