from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('index', 'title', 'question', 'solution', 'up', 'down')# 모델 파일을 이용해서 데이터를 JSON 형식에 맞도록 변환해주는 파일