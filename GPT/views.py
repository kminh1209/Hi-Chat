import os
import openai
import argparse
from dotenv import load_dotenv
from django.shortcuts import render
from q_food.views import Answer as QFoodAnswer



# class OpenAIGpt:
#   def __init__(spyelf):
#     load_dotenv()    

#   def run(self, args):
#     body = input("body : ")
#     question = input("Question : ")
#     text = f"{body} \n\nQ: {question}\nA:"
#     openai.api_key = os.getenv("API_KEY")
#     response = openai.Completion.create(
#       model="gpt-3.5-turbo-instruct",
#       prompt=f"{text}",
#       temperature=args.temperature,
#       max_tokens=100,      # 질문 길이 ( 보통 100자 = 토큰 200개)
#       top_p=1,
#       frequency_penalty=0.0,
#       presence_penalty=0.0,
#       stop=["\n"]
#     )
#     print(response)
#     print(response.choices[0].text.strip())


# if __name__ == '__main__':
#   parser = argparse.ArgumentParser()
#   # python gpt3.py --temperature 0.3
#   parser.add_argument('--temperature', default=0.3)

#   args = parser.parse_args()
#   openai_gpt = OpenAIGpt()
#   openai_gpt.run(args)


def product_print():
  # q_food 앱의 Answer 모델에서 데이터 가져오기
    q_food_answers = QFoodAnswer.objects.all()

    # 가져온 데이터를 출력하거나 다른 작업 수행
    for answer in q_food_answers:
        print(answer.answer_text)  
        # 예시로 answer_text를 출력하는데, 필드는 실제 모델에 맞게 변경하세요.


def your_view(request):
    # 데이터베이스에서 데이터 가져오기
    data_from_database = q_food.objects.all()

    # 가져온 데이터를 출력하거나 다른 작업 수행
    for item in data_from_database:
        print(item.q_food)  # 필드 이름은 실제 모델에 맞게 변경해야 합니다.

    # 원하는 렌더링 및 템플릿 로직 수행
    #return render(request, 'your_template.html', {'data_from_database': data_from_database})
