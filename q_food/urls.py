from django.urls import path
from . import views

app_name = 'q_food'

urlpatterns = [
    path('', views.index, name='index'),
    # path('delete_answers/', views.delete_answers, name='delete_answers'),  # 삭제 기능을 수행하는 URL 패턴 추가
    #path('<int:question_id>/', views.answer, name='answer'),
]

