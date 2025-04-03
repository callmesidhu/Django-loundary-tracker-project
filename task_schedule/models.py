from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=255)
    task_date = models.DateField()
    task_status = models.CharField(
        max_length=50, 
        choices=[('Pending', 'Pending'), ('Completed', 'Completed')]
    )
    task_time = models.TimeField()

    def __str__(self):
        return self.task
