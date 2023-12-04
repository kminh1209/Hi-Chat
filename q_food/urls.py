from django.urls import path
from . import views

app_name = 'q_food'

urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:question_id>/', views.answer, name='answer'),
]

