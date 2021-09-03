from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# 점수 총합에 해당하는 전역 변수
total_score = 0

def index(request):
    return render(request, 'index.html')

def quiz(request):
    questions = Question.objects.all() # 모델 전체를 가져옴.
    global total_score # 점수 총합
    
    return render(request, 'quiz.html', {"questions":questions, "total_score":total_score})

def checkbox_submit(request):
    if request.method == "POST":
        selected = request.POST.getlist('selected')

    return render


def result(request):
    global total_score
    if request.method == "POST":
        selected = request.POST.getlist('selected')
        selected = [ int(i) for i in selected ]
        total_score = sum(selected)
        print(total_score)

    return render(request,'result.html', {"total_score":total_score})


# 재형이가 처음에 짠 점수계산 코드

# 질문 전체를 가져와서 render로 띄워주기.
# def quiz(request):
#     questions = Question.objects.all() # 모델 전체를 가져옴.
#     global total_score # 점수 총합
    
   
#     return render(request, 'quiz.html', {"questions":questions, "total_score":total_score})

# 점수 알고리즘.
# def addScore(request, score): # 선택지에 해당하는 점수 == score,  html 선택지 링크에서 전달받음.
#     global total_score 
#     total_score += score
    
#     return redirect('quiz')

# 결과계산 원래 함수
# def result(request):
#     global total_score

#     return render(request,'result.html', {"total_score":total_score})