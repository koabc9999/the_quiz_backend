from rest_framework.response import Response
from rest_framework.decorators import api_view# 어떤 명령을 하고있는것인지 명시하는 데코레이터 부분
from .models import Quiz
from .serializers import QuizSerializer
from rest_framework.parsers import JSONParser
import random
from rest_framework import status

# Create your views here.
# 백엔드(DRF)의 기능적인 부분이 들어가는 파일

@api_view(['GET'])
def randomQuiz(request, id):# api 호출시 id로 전달받을 퀴즈의 수를 명시함
    totalQuizs = Quiz.objects.all()# 전체 퀴즈 모델로 가지고있는 데이터를 넣어줌
    randomQuizs = random.sample(list(totalQuizs), id)# random.sample 메소드를 활용해서 totalQuizs를 리스트를 변환해서 무작위로 하나 뽑아줌
    serializer = QuizSerializer(randomQuizs, many=True)# 모델에 맞는 시리얼라이져를 넣어서 시리얼라이져 변수를 선언해줌
    return Response(serializer.data)# 시리얼라이즈된 데이터를 Response의 내부에 넣어서 형식에 맞춰서 리턴해줌

@api_view(['GET'])# 전체 데이터를 쏴주는 뷰
def totalQuiz(request):
    totalQuizs = Quiz.objects.all()
    serializer = QuizSerializer(totalQuizs, many=True)
    return Response(serializer.data)

@api_view(['GET'])# 특정 데이터를 primary key로 불러오는 뷰
def theQuiz(request, pk):# primary key의 줄임말
    theQuiz = Quiz.objects.get(index=pk)# index의 값이 pk와 같은 object를 찾아서 theQuiz 변수에 넣어줌
    serializer = QuizSerializer(theQuiz, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getLatest(request):
    totalQuiz = Quiz.objects.all()# 전체 Quiz 오브젝트들을 변수에 넣음
    index = len(totalQuiz)# 전체 Quiz들의 크기를 변수에 저장
    latestQuiz = Quiz.objects.get(index=index)# index의 값이 퀴즈들 전체 Quiz 인스턴스 수와 같은 인스턴스를 변수에 넣어줌
    serializer = QuizSerializer(latestQuiz, many=False)# 시리얼라이저를 설정해줌
    return Response(serializer.data)

@api_view(['POST'])
def postQuiz(request):# 프런트에서 request를 받는것은 동일함
    serializer = QuizSerializer(data=request.data)# 시리얼라이저의 데이터에 request.data를 data로 넣어줌

    if serializer.is_valid():# 시리얼라이저 변수에 든 값이 유효하다면
        serializer.save()# 저장하는 함수를 실행
        return Response(serializer.data, status=status.HTTP_201_CREATED)# 넣어준 데이터를 return으로 화면에 띄워줌

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)# valid하지 않아서 분기하지 않았을 때 return 해주는 부분

@api_view(['POST'])
def updateQuiz(request, pk):# primary key를 통해서 특정 데이터를 서버에서 찾고 불러와서 수정해줌
    quiz = Quiz.objects.get(index=pk)# index의 값이 pk와 같은 Quiz 인스턴스를 불러와서 quiz변수에 넣어줌
    serializer = QuizSerializer(instance=quiz, data=request.data)# 넘겨받은 그 데이터에 request.data를 넣어줘서 수정되게함

    if serializer.is_valid():# 유효하게 serialize할 수 있으면
        serializer.save()# 데이터를 저장해줍니다
        return Response(serializer.data)# 저장한 데이터를 Response로 보내줍니다

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)