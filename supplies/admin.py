from django.contrib import admin
from .models import Towar

class TowarAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'obecna_ilosc', 'maksymalna_ilosc', 'potrzeba_domówić')


admin.site.register(Towar, TowarAdmin)