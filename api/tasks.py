# import random
# from celery import shared_task
# from .models import Car, Location
#
#
#
#
# def update_locations(json_data):
#     for truck in json_data:
#         latitude_offset = random.uniform(-0.01, 0.01)
#         longitude_offset = random.uniform(-0.01, 0.01)
#
#         truck['current_location']['latitude'] += latitude_offset
#         truck['current_location']['longitude'] += longitude_offset
#
#     return json_data
#
#
# @shared_task
# def update_car_locations():
#     """
#     Задача для случайного обновления локаций машин.
#     """
#     cars = Car.objects.all()
#     locations = Location.objects.all()
#
#     for car in cars:
#         # Выбираем случайное место из существующих
#         new_location = random.choice(locations)
#         car.current_location = new_location
#         car.save()
#
#     return f"Updated locations for {cars.count()} cars."

# import random
# from celery import shared_task
# from .models import Car
#
#
# def update_locations(cars):
#     """
#     Обновляет координаты машин в базе данных с небольшим случайным смещением.
#     """
#     for car in cars:
#         latitude_offset = random.uniform(-0.01, 0.01)
#         longitude_offset = random.uniform(-0.01, 0.01)
#
#         # Обновляем широту и долготу машины
#         car.current_location.latitude += latitude_offset
#         car.current_location.longitude += longitude_offset
#         car.current_location.save()  # Сохраняем изменения в локации
#
#     return f"Updated locations for {len(cars)} cars."
#
#
# @shared_task
# def update_car_locations():
#     """
#     Задача для обновления локаций машин.
#     """
#     cars = Car.objects.select_related('current_location').all()  # Выбираем машины вместе с их локациями
#     if not cars.exists():
#         return "No cars to update."
#
#     result = update_locations(cars)  # Обновляем координаты
#     return result
# from celery import shared_task
# import random
#
# from .models import Car
#
# # List of sample cities and states
# cities_and_states = [
#     ("New York", "New York"),
#     ("Chicago", "Illinois"),
#     ("Houston", "Texas"),
#     ("Los Angeles", "California"),
#     ("San Francisco", "California"),
#     # Add more as needed
# ]
#
# @shared_task
# def update_car_locations():
#     from .models import Car
#     cars = Car.objects.all()
#     for car in cars:
#         # Select a random city and state pair
#         city, state = random.choice(cities_and_states)
#
#         # Update the car's location
#         car.city = city
#         car.state = state
#         car.save()
#
#         # Optional: Print to confirm the update
#         print(f"Updated {car.unique_number}: {city}, {state}")
#
#     trucks = Car.objects.all()
#     for truck in trucks:
#         # Пример изменения координат
#         truck.latitude += random.uniform(-0.01, 0.01)
#         truck.longitude += random.uniform(-0.01, 0.01)
#         truck.save()

from __future__ import absolute_import, unicode_literals
from celery import shared_task
import random

from django.db import transaction

from .models import Car

# List of sample cities and states




from .models import Car, Location
from celery import shared_task
import random





@shared_task
def update_car_locations():
    # Получаем все существующие локации из базы данных
    locations = Location.objects.all()

    if not locations:
        print("Нет доступных локаций для обновления.")
        return

    # Получаем все машины из базы данных
    cars = Car.objects.all()

    for car in cars:
        # Выбираем случайную локацию из существующих локаций
        location = random.choice(locations)

        # Обновляем локацию автомобиля, присваивая объект Location
        car.current_location = location

        # Сохраняем обновленный объект автомобиля
        car.save()

        # Опционально: вывести информацию для отладки



