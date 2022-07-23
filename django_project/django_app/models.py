from django.utils import timezone
from django.db import models

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=150,unique=True)

class Employee(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150,default=None)
    date_of_birth=models.DateField(default=timezone.now())
    salary=models.IntegerField()
    department=models.ForeignKey(to=Department,on_delete=models.CASCADE)
    
