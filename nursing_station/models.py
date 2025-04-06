from django.db import models

class TaskSchedule(models.Model):
    uuid = models.CharField(max_length=5, primary_key=True)  # 5-digit UUID
    num_clothes = models.IntegerField()
    cloth_type = models.CharField(max_length=50)
    cloth_state = models.CharField(max_length=50)
    loading_a = models.CharField(max_length=20, default='pending')
    unloading_a = models.CharField(max_length=20, default='pending')
    loading_b = models.CharField(max_length=20, default='pending')
    unloading_b = models.CharField(max_length=20, default='pending')
    packing = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)  # current date & time

    def __str__(self):
        return self.uuid
