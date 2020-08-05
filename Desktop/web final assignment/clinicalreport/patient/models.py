from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_id = models.AutoField(auto_created = True, primary_key = True)
    fname = models.CharField(max_length = 100)
    lname = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100) 
    contact = models.CharField(max_length = 16)
    age = models.IntegerField()
    email = models.EmailField(max_length = 100)
    date = models.CharField(max_length = 100)

    class Meta:
        db_table = "patient"

