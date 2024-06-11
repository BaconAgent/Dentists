from django.urls import path
from .views import create_appointment, AppointmentListView

urlpatterns = [
    path('appointments/create', create_appointment, name='create-appointment'),
    path('appointments/<int:clinic_id>/', AppointmentListView.as_view(), name='list-appointments'),
]
