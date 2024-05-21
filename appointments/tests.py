from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class AppointmentTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_appointment(self):
        url = reverse("http://localhost:3000/appointments")
        data = {"clinicID": 1, "date": "2024-05-10", "time": "10:00", "userID": 1}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_appointment_with_invalid_data(self):
        url = reverse("http://localhost:3000/appointments")
        data = {"clinicID": 1, "date": "2024-04-01", "time": "10:00", "userID": 1}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
