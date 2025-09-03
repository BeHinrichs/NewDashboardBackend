from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="z.B. Berlin, Hamburg")
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class SunData(models.Model):
    # Jede Location hat genau einen Satz an Sonnen-Daten
    location = models.OneToOneField(Location, on_delete=models.CASCADE, primary_key=True)
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()
    date = models.DateField(auto_now=True) # Speichert das Datum der letzten Aktualisierung

    def __str__(self):
        return f"Sonnen-Daten für {self.location.name} am {self.date}"