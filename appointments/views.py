# appointments/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from clinic.models import Clinic
from user.models import User
from .models import Appointment
from .serializers import AppointmentSerializer


@api_view(['POST'])
def create_appointment(request):
    data = request.data
    user = User.objects.get(id=data['user_id'])
    clinic = Clinic.objects.get(id=data['clinic_id'])
    appointment = Appointment.objects.create(
        user=user,
        clinic=clinic,
        start_time=data['start_time'],
        end_time=data['end_time']
    )
    serializer = AppointmentSerializer(appointment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def list_appointments(request):
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)