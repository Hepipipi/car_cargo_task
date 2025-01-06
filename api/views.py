import django_filters
from django.shortcuts import render
from django_filters import filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Cargo, Car
from .serializers import CargoSerializer, CarSerializer
from geopy.distance import geodesic
from django_filters.rest_framework import DjangoFilterBackend

from django_filters import rest_framework as filters
from geopy.distance import geodesic
from .models import Cargo, Car

class CargoFilter(filters.FilterSet):
    min_distance = filters.NumberFilter(method='filter_min_distance', label='Минимальное расстояние (мили)')
    max_distance = filters.NumberFilter(method='filter_max_distance', label='Максимальное расстояние (мили)')
    min_weight = django_filters.NumberFilter(field_name="weight", lookup_expr='gte')
    max_weight = django_filters.NumberFilter(field_name="weight", lookup_expr='lte')

    class Meta:
        model = Cargo
        fields = ['min_distance', 'max_distance', 'min_weight', 'max_weight']

    def filter_min_distance(self, queryset, name, value):
        filtered_cargos = []
        cars = Car.objects.all()

        for cargo in queryset:
            for car in cars:
                distance = geodesic(
                    (cargo.pick_up.latitude, cargo.pick_up.longitude),
                    (car.current_location.latitude, car.current_location.longitude)
                ).miles
                if distance >= value:
                    filtered_cargos.append(cargo)
                    break

        return queryset.filter(id__in=[cargo.id for cargo in filtered_cargos])

    def filter_max_distance(self, queryset, name, value):
        filtered_cargos = []
        cars = Car.objects.all()

        for cargo in queryset:
            for car in cars:
                distance = geodesic(
                    (cargo.pick_up.latitude, cargo.pick_up.longitude),
                    (car.current_location.latitude, car.current_location.longitude)
                ).miles
                if distance <= value:
                    filtered_cargos.append(cargo)
                    break

        return queryset.filter(id__in=[cargo.id for cargo in filtered_cargos])





class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CargoFilter

    @action(detail=True, methods=['get'])
    def cars_nearby(self, request, pk=None):
        cargo = self.get_object()
        cars = Car.objects.all()
        nearby_cars = []

        for car in cars:
            distance = geodesic(
                (cargo.pick_up.latitude, cargo.pick_up.longitude),
                (car.current_location.latitude, car.current_location.longitude)
            ).miles
            if distance <= 450:
                nearby_cars.append({
                    'unique_number': car.unique_number,
                    'distance': distance
                })

        return Response(nearby_cars)

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer



