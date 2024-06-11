# appointments/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView

from clinic.models import Clinic
from .models import Appointment
from .serializers import AppointmentSerializer
from functools import wraps
import jwt
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]

    return token


def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, algorithms=['RS256'], verify=False)
            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response
        return decorated
    return require_scope


@api_view(['POST'])
# @requires_scope('create:appointments')
def create_appointment(request):
    data = request.data
    clinic = Clinic.objects.get(id=data['clinic_id'])
    appointment = Appointment.objects.create(
        user_id=data['user_id'],
        clinic_id=clinic,
        start_time=data['start_time'],
        end_time=data['end_time']
    )
    serializer = AppointmentSerializer(appointment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# @permission_classes([AllowAny])
# def list_appointments(request):
#     appointments = Appointment.objects.all()
#     serializer = AppointmentSerializer(appointments, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# @permission_classes([AllowAny])
# def list_appointments(request):
#     print(request.data)
#     appointments = Appointment.objects.filter(clinic_id=request.data['clinic_id'])
#     serializer = AppointmentSerializer(appointments, many=True)
#     return Response(serializer.data)
class AppointmentListView(APIView):
    def get(self, request, clinic_id):
        appointments = Appointment.objects.filter(clinic_id=clinic_id)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)