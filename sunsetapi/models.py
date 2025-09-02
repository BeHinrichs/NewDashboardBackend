from django.db import models

# Create your models here.
class Sunset(models.Model):
    date = models.DateField(verbose_name="von Datum")
    create_by = models.CharField(max_length=100, verbose_name="Von")
    title = models.CharField(max_length=120, verbose_name="Task", blank="false")
    status = models.CharField(max_length=100, verbose_name="Stauts")
    checked = models.BooleanField(default=False)