from rest_framework import serializers
from clinic.models import Clinic
from user.models import User
from .models import Appointment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email','password']


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['id', 'name', 'city', 'address']


class AppointmentSerializer(serializers.ModelSerializer):
    user: UserSerializer()
    clinic: ClinicSerializer

    class Meta:
        model = Appointment
        fields = ['id', 'user', 'clinic', 'start_time', 'end_time', 'created_at']
