from django.urls import path, include
from .views import randomQuiz, totalQuiz, theQuiz, getLatest, postQuiz, updateQuiz

urlpatterns = [
    path("<int:id>/", randomQuiz),# 127.0.0.1/3/ 이런식으로 주소가 넘어갈 수 있음
    path("all/", totalQuiz),# 전체 퀴즈를 받을 수 있는 url 주소
    path("the-quiz/<str:pk>/", theQuiz),# <int:pk>는 해당 위치에서 정수를 받아서 pk변수에 넣어서 전달해준다는 뜻
    path("get-latest/", getLatest),# 가장 나중에 추가된 퀴즈 인스턴스를 리턴해주는 view
    path("post-quiz/", postQuiz),# json 데이터를 넘겨받아서 request.data로 serializer를 통해서 추가해줌
    path("update-quiz/<str:pk>/", updateQuiz),# primary key를 넘겨받아서 거기에 request.data를 넣어줌
]