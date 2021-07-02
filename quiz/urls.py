from django.urls import path, include
from .views import helloAPI, randomQuiz

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),# 127.0.0.1/3/ 이런식으로 주소가 넘어갈 수 있음
]