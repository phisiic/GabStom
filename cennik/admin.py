from django.contrib import admin
from .models import Zabieg


class ZabiegAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'cena')


admin.site.register(Zabieg, ZabiegAdmin)
