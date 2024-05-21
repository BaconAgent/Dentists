from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_authenticated_endpoint(self):
        url = reverse("http://localhost:3000")
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_401_UNAUTHORIZED
        )  # Expecting 401 Unauthorized without token
