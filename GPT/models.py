# GPT/models.py
from django.db import models

class INFORMATION_Q(models.Model):
    # q_food 앱의 Question 모델과 동일한 필드를 정의
    question_text = models.CharField(max_length=200)
    url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.question_text


class INFORMATION_A(models.Model):
    # q_food 앱의 Answer 모델과 동일한 필드를 정의
    question = models.ForeignKey('q_food.Question', on_delete=models.CASCADE)
    answer_text = models.TextField()

    def __str__(self):
        return f"Answer for {self.question.question_text}"

