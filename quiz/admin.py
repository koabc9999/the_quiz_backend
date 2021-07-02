from django.contrib import admin
from .models import Quiz

# Register your models here.
# 관리자 페이지의 설정을 지정할 수 있는 파일
admin.site.register(Quiz)# Quiz 모델을 관리자 페이지에서 관리할 수 있게 해줌