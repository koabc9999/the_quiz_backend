from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random

# Create your views here.
# 백엔드(DRF)의 기능적인 부분이 들어가는 파일
@api_view(['GET'])
def helloAPI(request):
    return Response('hello world!')

@api_view(['GET'])
def randomQuiz(request, id):# api 호출시 id로 전달받을 퀴즈의 수를 명시함
    totalQuizs = Quiz.objects.all()# Quiz의 전체 오브젝트들을 변수에 넣어줌
    randomQuizs = random.sample(list(totalQuizs), id)# .sample 메소드가 첫번째 인자로 넘겨준 리스트 중에서 두번째 인자로 넘겨준 수 만큼 무작위로 뽑아줌
    serializer = QuizSerializer(randomQuizs, many=True)# 시리얼라이저에 random.sample로 선별된 리스트를 전달해줌 그러면 JSON화된 데이터가 변수에 저장됨
    return Response(serializer.data)