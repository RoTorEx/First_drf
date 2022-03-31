from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Women, Category
from .serializers import WomenSerializer


class WomenViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    '''Класс-представление позволяет избавиться от дублирования кода в предыдущих классах снизу.
    Этот класс позволяет реализовывать полный функцион (get, post) без идентификатора,
    и (put, delete) при добавлении ключа индетификатора.
    То етсь этот ОДИН класс заменяет все нижезакомментированные классы

    Если вместо "ModelViewSet" мы пропишем "ReadOnlyViewsSet", то мы сможем только читать записи.'''

    queryset = Women.objects.all()  # basename обязателен, если не указан атрибут querryset
    serializer_class = WomenSerializer

    '''Метод выборочного отображения запроса'''
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Women.objects.all()[:3]
        return Women.objects.filter(pk=pk)

    '''Предполагаем метод, который должен выводить список категорий
    Декоратор принимает поддерживаемые методы списком и определим вывод,
    True - вернёт одну запись, False - список
    Будет формировать такой маргрут – 127.0.0.1:8000/api/v1/women/category/'''
    @action(methods=['get'], detail=False)
    def category(self, request):  # Названия метода придумываем самостоятельно
        cats = Category.objects.all()  # Читаем все категории из модели категории
        return Response({'cats': [c.name for c in cats]})  # возвратим json ответ, перебираем из коллекции имена

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
