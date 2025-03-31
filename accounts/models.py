from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=128)
    
    class Meta:
        db_table = "employees"
