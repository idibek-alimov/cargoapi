from django.contrib import admin
from .models import Client, CalculatorData
# Register your models here.

# admin.site.register(Message)
admin.site.register(Client)
admin.site.register(CalculatorData)
