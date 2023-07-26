from django.shortcuts import render
from rest_framework import generics
from .models import Client, CalculatorData, Question, Feedback, MoscowPicture, ChinaPicture, Video
from .serializers import ClientSerializer, CalculatorDataSerializer, QuestionSerializer, FeedbackSerializer, MoscowPictureSerializer, ChinaPictureSerializer, VideoSerializer

from rest_framework.response import Response
from django.conf import settings
# Create your views here.
from .telegram_helper import Telegram
from django.views.decorators.csrf import csrf_exempt

# class MessageList(generics.ListCreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

#     def create(self, request):
#         serializer = MessageSerializer(data=request.data)
#         # Telegram.send_massage("hello motherfucker")
#         print("inside the create view")
#         if serializer.is_valid():
#             serializer.save()
#            # Telegram.send_massage(serializer.data["text"])
#             return Response({
#                 "message": serializer.data
#             })
#         else:
#             return Response({
#                 "error": serializer.errors
#             })


# class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

###############################################################


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @csrf_exempt
    def create(self, request):
        serializer = ClientSerializer(data=request.data)
        # Telegram.send_massage("hello motherfucker")
        # print("client creation")
        # print(request.data)
        if serializer.is_valid():
            serializer.save()
            # print(serializer.data)
            massage = "Имя: "+serializer.data["name"] + "\n"
            massage = massage + "Тел: "+serializer.data["number"] + "\n"
            massage = massage + "Комментарий: "+serializer.data["comment"]+"\n"
            if (serializer.data["deliveryMethod"] != None):
                massage = massage + "Способ доставки: " + \
                    serializer.data["deliveryMethod"] + "\n"
            # Telegram.send_massage(massage)
            return Response({
                "message": serializer.data
            })
        else:
            return Response({
                "error": serializer.errors
            })
#######################################################################


class CalculatorDataList(generics.ListCreateAPIView):
    queryset = CalculatorData.objects.all()
    serializer_class = CalculatorDataSerializer

    @csrf_exempt
    def create(self, request):
        serializer = CalculatorDataSerializer(data=request.data)
        # Telegram.send_massage("hello motherfucker")
        print("calculator creation")
        print(request.data)

        if serializer.is_valid():
            serializer.save()
            massage = "Имя: "+serializer.data["name"] + "\n"
            massage = massage + "Тел: "+serializer.data["number"] + "\n"
            massage = massage + "Тип продукта: " + \
                serializer.data["productType"] + "\n"
            massage = massage + "Имя продукта: " + \
                serializer.data["productName"] + "\n"
            massage = massage + "Количества: " + \
                str(serializer.data["quantity"]) + "\n"
            massage = massage + "Масса: " + \
                str(serializer.data["mass"]) + "кг" + "\n"
            massage = massage + "Способ доставки: " + \
                serializer.data["deliveryMethod"] + "\n"
            massage = massage + "Адрес: " + serializer.data["address"] + "\n"
            if (serializer.data["insurance"] != False):
                massage = massage + "Страховка: " + "Да" + "\n"
            else:
                massage = massage + "Страховка: " + "Нет" + "\n"
            if (serializer.data["deliveryPrice"] != None):
                massage = massage + "Цена: " + \
                    str(serializer.data["deliveryPrice"]) + "\n"
            if (serializer.data["deliveryTime"] != None):
                massage = massage + "Время доставки: " + \
                    str(serializer.data["deliveryTime"]) + "\n"

            massage = massage + "Комментарий: "+serializer.data["comment"]+"\n"

            # if (serializer.data["deliveryMethod"] != None):
            #     massage = massage + "Способ доставки: " + \
            #         serializer.data["deliveryMethod"] + "\n"
            print(serializer.data)
            # Telegram.send_massage(massage)
            return Response({
                "message": serializer.data
            })
        else:
            return Response({
                "error": serializer.errors
            })


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class ChinaPictureList(generics.ListCreateAPIView):
    queryset = ChinaPicture.objects.all()
    serializer_class = ChinaPictureSerializer


class MoscowPictureList(generics.ListCreateAPIView):
    queryset = MoscowPicture.objects.all()
    serializer_class = MoscowPictureSerializer


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
