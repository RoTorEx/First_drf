from django.shortcuts import render
from rest_framework import generics
from .serializers import WomenSerializer
from .models import Women
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets


# class WomenViewSet(viewsets.ModelViewSet):
class WomenViewSet(viewsets.ReadOnlyModelViewSet):

    '''Класс-представление позволяет избавиться от дублирования кода в предыдущих классах снизу.
    Этот класс позволяет реализовывать полный функцион (get, post) без идентификатора,
    и (put, delete) при добавлении ключа индетификатора.
    То етсь этот ОДИН класс заменяет все нижезакомментированные классы

    Если вместо "ModelViewSet" мы пропишем "ReadOnlyViewsSet", то мы сможем только читать записи.'''

    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# class WomenAPIList(generics. ListCreateAPIView):

#     '''Упрощённый класс представления API методов. Наследуется от базового класса ListCreateAPIView.
#     Этот класс будет как возвращать список записей, так и возвращать и их по пост запросу.'''

#     # Этих двух моментов достаточно чтобы получить функциональность
#     queryset = Women.objects.all()  # Ссылается на список записей возвращаемых клиенту
#     serializer_class = WomenSerializer  # Тот сериализатор, который мы будем применять к объекту


# class WomenAPIUpdate(generics.UpdateAPIView):

#     '''Класс-представление изменющий записи в базе данных (метод put or patch), заменяющий класс снизу'''

#     queryset = Women.objects.all()  # Получает набор всех данных из таблицы. Это "ленивый" запрос
#     serializer_class = WomenSerializer  # Класс сериализатора


# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):

#     '''Класс-представления наследуется от класса и позволяет получить, изменить и удалить данные (CRUD).
#     Поддерживают методы get, put, patch, delete. То есть так для одной записи мы делаем несколько действий.

#     Без DRF пришлось бы писать куда больше кода.'''

#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
