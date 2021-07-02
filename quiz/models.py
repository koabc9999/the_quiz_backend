from django.db import models

# Create your models here.
class Quiz(models.Model):# 자료의 형식을 파이썬 내부적으로 선언하는 파일
    index = models.IntegerField()
    title = models.CharField(max_length=200)
    question = models.TextField()
    solution = models.TextField()
    up = models.IntegerField()
    down = models.IntegerField()
# 처음으로 퀴즈 모델이 사용되기 시작할 때는 migration을 해줘야함