from django.db import models


# Create your models here.
class Patient(models.Model):
    patient_first_name = models.CharField(max_length=200)
    patient_last_name = models.CharField(max_length=200)
    patient_birthdate = models.DateField()
    # workaround to enable syntax highlighting in PyCharm Community (explicitly expose django model manager)
    objects = models.Manager()

    def __str__(self):
        return "Patient : " + str(self.patient_first_name) + \
            " " + str(self.patient_last_name) + \
            " Born: " + str(self.patient_birthdate)
