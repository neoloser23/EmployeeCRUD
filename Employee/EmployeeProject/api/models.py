from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
