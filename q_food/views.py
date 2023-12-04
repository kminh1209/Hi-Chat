from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Answer

# def index(request):
#     questions = Question.objects.all()
#     return render(request, 'q_food/index.html', {'questions': questions})

# def answer(request, question_id): # 각각의 질문에 대한 답변을 처리하는 구조
#     question = get_object_or_404(Question, pk=question_id)
    
#     if request.method == 'POST':
#         answer_text = request.POST.get('answer_text', '')
#         Answer.objects.create(question=question, answer_text=answer_text)
#         return redirect('q_food:detail', question_id=question.id)

#     return render(request, 'q_food/answer.html', {'question': question})

def index(request): # 여러 질문에 대한 답변을 한 번에 입력받아 처리하고자 하는 경우
    questions = Question.objects.all()

    if request.method == 'POST':
        for question in questions:
            answer_text = request.POST.get(f'answer_{question.id}', '')
            Answer.objects.create(question=question, answer_text=answer_text)

    return render(request, 'q_food/index.html', {'questions': questions})

# DB 삭제를 위한 함수
# def delete_answers(request):
#     if request.method == 'POST':
#         # 사용자 입력 받은 정보를 데이터베이스에서 삭제
#         Answer.objects.all().delete()

#     return redirect('q_food:index')  # 삭제 후 index 페이지로 리디렉션