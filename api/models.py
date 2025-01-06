from django.db import models

class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.city}, {self.state} ({self.zip_code})"

class Car(models.Model):
    unique_number = models.CharField(max_length=10, unique=True)
    current_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    load_capacity = models.IntegerField()

    def __str__(self):
        return self.unique_number

class Cargo(models.Model):
    pick_up = models.ForeignKey(Location, related_name='pick_up', on_delete=models.SET_NULL, null=True, blank=True)
    delivery = models.ForeignKey(Location, related_name='delivery', on_delete=models.SET_NULL, null=True, blank=True)
    weight = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"Cargo {self.id} ({self.weight} kg)"








