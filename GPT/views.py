import os
import openai
import argparse
from django.http import JsonResponse
from dotenv import load_dotenv
from django.shortcuts import render
from q_food.models import Question, Answer



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

def data_b():
    # Question 모델에서 데이터를 가져와서 질문에 대한 답변을 얻습니다.
    try:
        # 예시로 가장 최근의 데이터를 가져오는 방법입니다.
        latest_question = Question.objects.latest('id')
        answer = Answer.objects.get(question=latest_question)
        answer_text = answer.answer_text
    except (Question.DoesNotExist, Answer.DoesNotExist):
        answer_text = "No answer found."

    return answer_text

def some_view(request):
    answer_text = data_b()

    # 예시로 가장 최근의 질문을 가져오는 방법입니다.
    try:
        latest_question = Question.objects.latest('id')
        question_text = latest_question.question_text
    except Question.DoesNotExist:
        question_text = "No question found."

    # 템플릿 렌더링
    return render(request, 'GPT/index.html', {'question_text': question_text, 'answer_text': answer_text})

# def some_view(request):
#     # 예시로 모델 인스턴스를 가져옴
#     info_q_instance = INFORMATION_Q.objects.get(pk=1)
#     info_a_instance = INFORMATION_A.objects.get(pk=1)

#     # to_dict 메서드를 사용하여 딕셔너리로 변환
#     info_q_dict = info_q_instance.to_dict()
#     info_a_dict = info_a_instance.to_dict()

#     # JSON 응답 생성
#     response_data = {
#         'info_q': info_q_dict,
#         'info_a': info_a_dict,
#     }

#     return JsonResponse(response_data)