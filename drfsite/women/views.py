from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .models import Women, Category
from .serializers import WomenSerializer
from .permissions import *


class WomenAPIList(generics.ListCreateAPIView):
    '''Возвращает запись'''
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # Строка запрещает редактиврование статей через API неавторизированным пользователям
    permission_classes = (IsAuthenticatedOrReadOnly, )


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    '''Обновляет запись'''
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # Ссылаемся на собсвенный класс
    permission_classes = (IsOwnerOrReadOnly, )


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    '''Удаляеть запись'''
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # Удалять записи может только администратор сайта, но тогда просматривать никто не сможет
    permission_classes = (IsAdminOrReadOnly, )


# class WomenViewSet(mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.ListModelMixin,
#                    viewsets.GenericViewSet):

#     '''Класс-представление позволяет избавиться от дублирования кода в предыдущих классах снизу.
#     Этот класс позволяет реализовывать полный функцион (get, post) без идентификатора,
#     и (put, delete) при добавлении ключа индетификатора.
#     То етсь этот ОДИН класс заменяет все нижезакомментированные классы

#     Если вместо "ModelViewSet" мы пропишем "ReadOnlyViewsSet", то мы сможем только читать записи.'''

#     queryset = Women.objects.all()  # basename обязателен, если не указан атрибут querryset
#     serializer_class = WomenSerializer

#     '''Метод выборочного отображения запроса'''
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#         if not pk:
#             return Women.objects.all()[:3]
#         return Women.objects.filter(pk=pk)

#     '''Предполагаем метод, который должен выводить список категорий
#     Декоратор принимает поддерживаемые методы списком и определим вывод,
#     True - вернёт одну запись, False - список
#     Будет формировать такой маргрут – 127.0.0.1:8000/api/v1/women/category/'''
#     @action(methods=['get'], detail=False)
#     def category(self, request):  # Названия метода придумываем самостоятельно
#         cats = Category.objects.all()  # Читаем все категории из модели категории
#         return Response({'cats': [c.name for c in cats]})  # возвратим json ответ, перебираем из коллекции имена
