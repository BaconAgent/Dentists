from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from appointments.serializers import ClinicSerializer
from clinic.models import Clinic


# class ClinicListView(APIView):
#     def get(self, request):
#         clinics = Clinic.objects.all()
#         serializer = ClinicSerializer(clinics, many=True)
#         return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_clinics(request):
    clinics = Clinic.objects.all()
    serializer = ClinicSerializer(clinics, many=True)
    return Response(serializer.data)
