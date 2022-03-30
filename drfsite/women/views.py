from django.shortcuts import render
from rest_framework import generics
from .serializers import WomenSerializer
from .models import Women
from rest_framework.response import Response
from rest_framework.views import APIView


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


class WomenAPIView(APIView):

    '''APIView стоит во главе всех классов предствления API в рамках Django REST Framework'''

    # Этот метод обрабатывает GET запросы поступающие на сервер
    def get(self, request):
        # Формирование строки JSON
        # return Response({'title': 'Angelina Jolie'})
        # Здесь выбираем все записи из таблицы women, преобразуем их к списку и возвращаем в виде JSON-строки
        lst = Women.objects.all().values()
        return Response({'posts': list(lst)})

    # Этот метод обрабатывает POST запросы
    def post(self, request):
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )

        return Response({'post': model_to_dict(post_new)})
