from django.db import models

from clinic.models import Clinic
from user.models import User


# Create your models here.


class Appointment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment from {self.start_time} to {self.end_time}"
