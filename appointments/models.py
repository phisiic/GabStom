from django.db import models
from datetime import datetime
from accounts.models import User
from cennik.models import Zabieg
from django.core.exceptions import ValidationError


TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_article_set')
    doctor = models.CharField(max_length=50, null=True, blank=True)
    service = models.CharField(max_length=255, null=True, blank=True)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)

    def clean(self, *args, **kwargs):
        super(Appointment, self).clean(*args, **kwargs)

        if self.time < datetime.now():
            raise ValidationError('Nieprawidłowa data wizyty.')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} | {self.day} | {self.time}"
