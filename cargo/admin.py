from django.contrib import admin
from .models import Client, CalculatorData, Question, Feedback, MoscowPicture, ChinaPicture, Video
# Register your models here.

# admin.site.register(Message)
admin.site.register(Client)
admin.site.register(CalculatorData)
admin.site.register(Question)
admin.site.register(Feedback)
admin.site.register(MoscowPicture)
admin.site.register(ChinaPicture)
admin.site.register(Video)
