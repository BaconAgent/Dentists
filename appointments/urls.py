from django.urls import path
from .views import create_appointment, list_appointments

urlpatterns = [
    path('appointments/create', create_appointment, name='create-appointment'),
    path('appointments/', list_appointments, name='list-appointments'),
]
