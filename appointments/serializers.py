from rest_framework import serializers
from clinic.models import Clinic
from .models import Appointment


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['id', 'name', 'city', 'address']


class AppointmentSerializer(serializers.ModelSerializer):
    clinic: ClinicSerializer

    class Meta:
        model = Appointment
        fields = ['id', 'user_id', 'clinic_id', 'start_time', 'end_time', 'created_at']
