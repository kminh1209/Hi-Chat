# 데이터베이스에서 객체를 가져오거나, 존재하지 않을 경우 404 에러를 반환
from django.shortcuts import get_object_or_404, get_list_or_404
# api_view 데코레이터를 import, 데코레이터:함수 기반의 뷰를 API 뷰로 변환해줌
from rest_framework.decorators import api_view
# API 응답을 생성하는데 사용됨
from rest_framework.response import Response
# HTTP 상태 코드를 제공
from rest_framework import status
# Django 프로젝트의 설정을 관리하는데 사용됨
from django.conf import settings
import requests, json

API_KEY = settings.API_KEY #외부 API에 대한 인증

# @api_view 데코레이터를 적용하여 GET 메서드만 허용하는 API 뷰로 설정
@api_view(['GET'])  
def products(request):
    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': '1'
    }
    response = requests.get(url, params=params)
    response_data = response.json()

    if 'result' in response_data:
        products_data = response_data['result'].get('baseList', [])
    else:
        products_data = []

    return Response(products_data)
