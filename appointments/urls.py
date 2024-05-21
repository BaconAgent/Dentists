from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', create_appointment, name='create-appointment'),
]
