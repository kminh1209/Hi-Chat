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

