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


class Wizyta(models.Model):
    user = models.ForeignKey(User, verbose_name="Użytkownik", on_delete=models.CASCADE, null=True, blank=True, related_name='user_article_set')
    doctor = models.CharField(max_length=50, null=True, blank=True, verbose_name="Lekarz")
    service = models.CharField(max_length=255, null=True, blank=True, verbose_name="Zabieg")
    day = models.DateField(default=datetime.now, verbose_name="Data")
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM", verbose_name="Czas")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True, verbose_name="Data rejestracji")

    def clean(self, *args, **kwargs):
        super(Wizyta, self).clean(*args, **kwargs)

        if self.day < datetime.now():
            raise ValidationError('Nieprawidłowa data wizyty.')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} | {self.day} | {self.time}"

    class Meta:
        verbose_name_plural = "Wizyty"
