# q_food앱의 모델 데이터를 GPT 앱의 모델로 다 끌고 오기 위한 Script code 
import os
import django

# 설정을 불러와야 함
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# GPT 앱의 models.py에서 INFORMATION_A과 INFORMATION_Q 모델을 import
from GPT.models import INFORMATION_A, INFORMATION_Q

# q_food 앱의 Answer와 Question 모델을 import
from q_food.models import Answer as QFoodAnswer, Question as QFoodQuestion

# q_food 앱의 데이터를 가져와서 GPT 앱에 저장
for q_food_answer in QFoodAnswer.objects.all():
    INFORMATION_A.objects.create(
        question=q_food_answer.question,
        answer_text=q_food_answer.answer_text
    )

for q_food_question in QFoodQuestion.objects.all():
    INFORMATION_Q.objects.create(
        question_text=q_food_question.question_text,
        url=q_food_question.url
    )

print("Data copied successfully.")
