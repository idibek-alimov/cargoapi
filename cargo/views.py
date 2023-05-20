from django.shortcuts import render
from rest_framework import generics
from .models import Client, CalculatorData
from .serializers import ClientSerializer, CalculatorDataSerializer
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
        print("client creation")
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            Telegram.send_massage(serializer.data)
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
            print(serializer.data)
            Telegram.send_massage(serializer.data)
            return Response({
                "message": serializer.data
            })
        else:
            return Response({
                "error": serializer.errors
            })
