import os
import openai
from django.shortcuts import render
from dotenv import load_dotenv
from q_food.models import Question, Answer

def all_data():
    questions = Question.objects.all()
    data = []
    for i, question in enumerate(questions, start=1):
        answers = Answer.objects.filter(question=question)
        answer_text = answers.last().answer_text if answers else "No answer found."
        data.append(f"질문{i}: {question.question_text}답변: {answer_text}")
    return data

class OpenAIGpt:
    def __init__(self):
        load_dotenv()

    def run(self, body, question, args):
        text = f"{body} \n\nQ: {question}\nA:"
        openai.api_key = os.getenv("API_KEY")
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"{text}",
            temperature=args.temperature,
            max_tokens=3000,      # 질문 길이 ( 보통 100자 = 토큰 200개)
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\n"]
        )
        return response.choices[0].text.strip()

def some_view(request):
    # OpenAIGpt 클래스의 인스턴스 생성
    openai_gpt = OpenAIGpt()

    # argparse 모듈을 사용하여 더미 args를 생성
    class DummyArgs:
        temperature = 0.3  # 적절한 값을 설정해야 함

    # 더미 args를 사용하여 OpenAIGpt의 run 메소드 호출
    body = "\n".join(all_data())
    question = "중요:문자수 공백제외 2000으로 제한하지 말고 그 이상으로 작성해줘. 식품회사의 인재상이 책임감 있고, 지속적으로 발전하려는 자세를 갖은 사람이라는 것을 기억하고 자기소개서를 써줘."
    api_output = openai_gpt.run(body, question, DummyArgs())

# 템플릿 렌더링
    return render(request, 'GPT/index.html', {'api_output': api_output})