from rest_framework import serializers
from .models import Cargo, Car, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['city', 'state', 'zip_code', 'latitude', 'longitude']

class CarSerializer(serializers.ModelSerializer):
    current_location = LocationSerializer()

    class Meta:
        model = Car
        fields = ['unique_number', 'current_location', 'load_capacity']


class CargoSerializer(serializers.ModelSerializer):
    pick_up = LocationSerializer()
    delivery = LocationSerializer()

    class Meta:
        model = Cargo
        fields = ['pick_up', 'delivery', 'weight', 'description']
