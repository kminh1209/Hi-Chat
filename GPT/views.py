import os
import openai
import argparse
from django.http import JsonResponse
from dotenv import load_dotenv
from django.shortcuts import render
from q_food.models import Question, Answer

def all_data():
    # Question 모델에 대한 모든 데이터를 가져옵니다.
    questions = Question.objects.all()

    data = []
    for question in questions:
        # Question과 연결된 모든 Answer를 가져옵니다.
        answers = Answer.objects.filter(question=question)

        # Answer 객체가 하나 이상 있는 경우, 가장 최근의 Answer를 사용합니다.
        answer_text = answers.last().answer_text if answers else "No answer found."

        data.append({
            'question_text': question.question_text,
            'answer_text': answer_text
        })

    return data

def some_view(request): #특정 URL에 대한 요청이 들어왔을 때 실행되어 사용자에게 데이터를 제공하는 역할
    all_data_list = all_data()

    # 템플릿 렌더링
    return render(request, 'GPT/index.html', {'all_data_list': all_data_list})



# class OpenAIGpt:
#   def __init__(spyelf):
#     load_dotenv()    

#   def run(self, args):
#     body = input("정보 : ")
#     question = input("요구 : ")
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

