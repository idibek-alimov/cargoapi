from rest_framework import serializers
from .models import Client, CalculatorData, Question, Feedback, MoscowPicture, ChinaPicture, Video

# class MessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Message
#         fields = ("__all__")


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("__all__")


class CalculatorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculatorData
        fields = ("__all__")


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("__all__")


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("__all__")


class MoscowPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoscowPicture
        fields = ("__all__")


class ChinaPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChinaPicture
        fields = ("__all__")


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ("__all__")
