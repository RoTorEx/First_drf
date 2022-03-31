from django.shortcuts import render
from rest_framework import generics
from .serializers import WomenSerializer
from .models import Women
from rest_framework.response import Response
from rest_framework.views import APIView


# class WomenAPIView(APIView):

#     '''APIView стоит во главе всех классов предствления API в рамках Django REST Framework'''

#     # Этот метод обрабатывает GET запросы поступающие на сервер
#     def get(self, request):
#         # Формирование строки JSON
#         # return Response({'title': 'Angelina Jolie'})
#         # Здесь выбираем все записи из таблицы women, преобразуем их к списку и возвращаем в виде JSON-строки
#         lst = Women.objects.all().values()
#         return Response({'posts': list(lst)})

#     # Этот метод обрабатывает POST запросы
#     def post(self, request):
#         post_new = Women.objects.create(
#             title=request.data['title'],
#             content=request.data['content'],
#             cat_id=request.data['cat_id']
#         )

#         return Response({'post': model_to_dict(post_new)})


class WomenAPIView(APIView):

    ''''''

    def get(self, request):
        # ФОрмируем список объектов класса Women
        w = Women.objects.all()  # Список статей получаем как набор queryset
        # Передаём весь список на сериализатор. Response преобразовывает всё в байтовую JSON строку
        # Response вызывает JSON render и преобразовывает данные
        return Response({'posts': WomenSerializer(w, many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        # Проверка корректности принятных данных, если каких-то данных не будет хватать в запросе,
        # то будет сгенерированно исключение
        serializer.is_valid(raise_exception=True)

        # Если проверка прошла успешно, то добавляем данные в базу данных
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )

        # Возвращаем то, что было добавлено
        return Response({'post': WomenSerializer(post_new).data})
