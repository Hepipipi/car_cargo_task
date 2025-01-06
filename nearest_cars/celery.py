from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установка стандартных настроек Django для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nearest_cars.settings')

app = Celery('nearest_cars')

# Настройки Celery
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.worker_concurrency = 1


# Автоматический поиск задач в приложениях Django
app.autodiscover_tasks()

app.conf.update(
    worker_pool='solo',
)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
