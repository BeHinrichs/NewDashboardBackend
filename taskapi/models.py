from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=20, verbose_name="Für")
    create_by = models.CharField(max_length=20, verbose_name="Von")
    title = models.CharField(max_length=120, verbose_name="Task", blank="false")
    status = models.CharField(max_length=20, verbose_name="Stauts")
    checked = models.BooleanField(default=False)