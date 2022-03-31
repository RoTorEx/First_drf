from django.shortcuts import render
from rest_framework import generics
from .serializers import WomenSerializer
from .models import Women
from rest_framework.response import Response
from rest_framework.views import APIView


class WomenAPIList(generics. ListCreateAPIView):

    '''Упрощённый класс представления API методов. Наследуется от базового класса ListCreateAPIView.
    Этот класс будет как возвращать список записей, так и возвращать и их по пост запросу.'''

    # Этих двух моментов достаточно чтобы получить функциональность
    queryset = Women.objects.all()  # Ссылается на список записей возвращаемых клиенту
    serializer_class = WomenSerializer  # Тот сериализатор, который мы будем применять к объекту


class WomenAPIUpdate(generics.UpdateAPIView):

    '''Класс-представление изменющий записи в базе данных (метод put or patch), заменяющий класс снизу'''

    queryset = Women.objects.all()  # Получает набор всех данных из таблицы. Это "ленивый" запрос
    serializer_class = WomenSerializer  # Класс сериализатора


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):

    '''Класс-представления наследуется от класса и позволяет получить, изменить и удалить данные (CRUD).
    Поддерживают методы get, put, patch, delete. То есть так для одной записи мы делаем несколько действий.
    
    Без DRF пришлось бы писать куда больше кода.'''

    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# class WomenAPIView(APIView):

#     '''Класс сериализатор'''

#     # Метод отправки данных с базы данных клиенту
#     def get(self, request):
#         # ФОрмируем список объектов класса Women
#         w = Women.objects.all()  # Список статей получаем как набор queryset
#         # Передаём весь список на сериализатор. Response преобразовывает всё в байтовую JSON строку
#         # Response вызывает JSON render и преобразовывает данные
#         return Response({'posts': WomenSerializer(w, many=True).data})

#     # Метод для добавления новых данных
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         # Проверка корректности принятных данных, если каких-то данных не будет хватать в запросе,
#         # то будет сгенерированно исключение
#         serializer.is_valid(raise_exception=True)
#         serializer.save()  # Запись в базу данных

#         # Возвращаем то, что было добавлено и коллекция data будет ссылаться на новый созданный объект
#         return Response({'post': serializer.data})

#     # Метод для обноваления данных в базе данных
#     def put(self, request, *args, **kwargs):
#         # Идентификатор записи, которую нужно поменять
#         pk = kwargs.get("pk", None)
#         # Если ключ pk не присутсвует то мы не можем выполнить метод put для изменения записи 
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})

#         # Пробуем взять запись из модели Women
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})

#         # Если всё было успешно получено и пройдено, то создаём сериализатор
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()  # Автоматически вызовет в сериализаторе метод update

#         return Response({"post": serializer.data})

#     # Метод для удаления данных из базы данных
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})

#         # здесь код для удаления записи с переданным pk

#         return Response({"post": "delete post " + str(pk)})
