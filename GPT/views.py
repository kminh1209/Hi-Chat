from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests, json

API_KEY = settings.API_KEY

@api_view(['GET'])
def products(request):
    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': '1'
    }
    response = requests.get(url, params=params)
    products_data = response.json()['result']['baseList']
    
    return Response(products_data)
