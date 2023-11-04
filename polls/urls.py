from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.index, name='index'),        # => views.index라는 views내부로 연결
]
