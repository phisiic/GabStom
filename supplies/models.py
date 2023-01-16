from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Towar(models.Model):
    nazwa = models.CharField(max_length=255)
    maksymalna_ilosc = models.PositiveIntegerField()
    obecna_ilosc = models.PositiveIntegerField()
    potrzeba_domówić = models.BooleanField()

    def clean(self):
        if self.obecna_ilosc > self.maksymalna_ilosc:
            raise ValidationError("Obecna ilość przekracza maksymalną")

    def save(self, *args, **kwargs):
        if self.obecna_ilosc < 0.3*self.maksymalna_ilosc:
            self.potrzeba_domówić = True
        else:
            self.potrzeba_domówić = False
        super(Towar, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Towar"

