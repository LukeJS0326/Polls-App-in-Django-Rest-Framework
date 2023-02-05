from rest_framework import serializers
from .models import Question
from .models import Choice

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'question_text',
            'pub_date',
        )
        model = Question
class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionSerializer
    class Meta:
        model = Choice
        fields ='__all__'
