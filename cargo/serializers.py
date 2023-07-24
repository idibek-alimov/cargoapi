from rest_framework import serializers
from .models import Client, CalculatorData, Question, Feedback

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
