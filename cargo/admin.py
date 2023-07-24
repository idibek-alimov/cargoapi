from django.contrib import admin
from .models import Client, CalculatorData, Question, Feedback
# Register your models here.

# admin.site.register(Message)
admin.site.register(Client)
admin.site.register(CalculatorData)
admin.site.register(Question)
admin.site.register(Feedback)
