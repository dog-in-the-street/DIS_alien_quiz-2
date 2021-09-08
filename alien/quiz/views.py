from django.shortcuts import render, redirect, get_object_or_404
from .models import Question

# 점수 총합에 해당하는 전역 변수
total_score = 0

def index(request):
    return render(request, 'index.html')


def quiz(request):
    questions = Question.objects.all() # 모델 전체를 가져옴.
    global total_score # 점수 총합
        
    return render(request, 'quiz.html', {"questions":questions, "total_score":total_score})

# def checkbox_submit(request):
#     if request.method == "POST":
#         selected = request.POST.getlist('selected')

#     return render(reques)

# 결과 페이지 html render
def rock(request):
    return render(request, 'result/rock.html')


def raccoon(request):
    return render(request, 'result/raccoon.html')


def martian(request):
    return render(request, 'result/martian.html')


def baby(request):
    return render(request, 'result/baby.html')


def president(request):
    return render(request, 'result/president.html')


def wizard(request):
    return render(request, 'result/wizard.html')


def dog(request):
    return render(request, 'result/dog.html')


def result(request):
    # 점수 산출
    global total_score
    if request.method == "POST":
        selected = request.POST.getlist('selected[]')
        selected = [ int(i) for i in selected ]
        total_score = sum(selected)
    # 돌 유형 0 ~ 20
    if total_score >= 0 and total_score < 35:
        return redirect('rock')
    # 라쿤 유형 21 ~ 40
    elif total_score >= 36 and total_score < 50:
        return redirect('raccoon')
    # 화성인 유형 41 ~ 60
    elif total_score >= 51 and total_score < 65:
        return redirect('martian')
    # 애기 외계인 유형 61 ~ 80
    elif total_score >= 66 and total_score < 80:
        return redirect('baby')
    # 외계인 협회장 유형 81 ~ 100
    elif total_score >= 81 and total_score < 100:
        return redirect('president')
    # 대마법사 유형 <2000
    elif total_score >= 100 and total_score < 2000:
        return redirect('wizard')
    # 저잣거리를 떠도는 개 유형 <50000
    elif total_score >= 2000 and total_score < 50000:
        return redirect('dog')

        #35,50,65,80,100
    # 에러처리
    else:
        error = "정상적인 페이지 접근이 아닙니다."
        return render(request,'result.html',{'error':error})







# 테스트 다시하기
# def reset(request):
#     global total_score
#     total_score = 0 # 점수 0으로 초기화시키기.
#     return redirect('index') # redirect하는 페이지의 url name을 넣어주기.

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

def DIS(request):
    return render(request,'DIS.html')