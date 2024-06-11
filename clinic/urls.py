from django.urls import path
from .views import get_clinics
urlpatterns = [
    path('clinics/', get_clinics, name='clinic-list'),
]
