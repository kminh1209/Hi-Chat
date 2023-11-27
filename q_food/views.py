from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Answer

def index(request):
    questions = Question.objects.all()
    return render(request, 'q_food/index.html', {'questions': questions})

def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        answer_text = request.POST['answer_text']
        Answer.objects.create(question=question, answer_text=answer_text)
        return HttpResponseRedirect(reverse('Question:index'))
    return render(request, 'Question/answer.html', {'question': question})
