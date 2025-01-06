from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CargoViewSet, CarViewSet

router = DefaultRouter()
router.register('cargo', CargoViewSet)
router.register('cars', CarViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
