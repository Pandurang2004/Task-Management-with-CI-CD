from django.db import models

# Create your models here.
class TaskModels(models.Model):
    task_name = models.CharField(max_length=30)
    task_descp = models.TextField(max_length=100)
    task_added_at = models.DateTimeField(auto_now_add=True)
    task_status = models.BooleanField(default=False)
