import csv
from django.core.management.base import BaseCommand
from .models import Location


class Command(BaseCommand):
    help = 'Загружает данные из uszips.csv в модель Location'

    def handle(self, *args, **kwargs):
        file_path = r'C:\Users\User\OneDrive\Рабочий стол\e\nearest_cars\uszips.csv'

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            locations = []

            for row in reader:
                locations.append(
                    Location(
                        city=row['city'],
                        state=row['state_id'],
                        zip_code=row['zip'],
                        latitude=float(row['lat']),
                        longitude=float(row['lng'])
                    )
                )

            Location.objects.bulk_create(locations, ignore_conflicts=True, batch_size=1000)

        self.stdout.write(self.style.SUCCESS('Locations loaded successfully'))
