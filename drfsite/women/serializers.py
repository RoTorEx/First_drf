import io

from rest_framework import serializers
from .models import Women
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# class WomenModel:

#     '''Объекты этого класса мы будем сериализовать, то есть преобразовывать в json строку.
#     Этот класс будет как бы имитировать модели фреймворка Django'''

#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.Serializer):

    '''Класс-сериализатор для модели women. С помощью которого преобразуем объекты моделей в словарь,
    а затем его в json строку с помощью json render'''

    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)  # Параметры только для чтения
    time_update = serializers.DateTimeField(read_only=True)  # Параметры только для чтения
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()


# class WomenSerializer(serializers.Serializer):

#     '''Наследуется от серелизатора, который работает с моделями'''
#     class Meta:

#         model = Women
#         # Ниже приведены поля для серилизации, то есть те,
#         # котрые будут отправляться обратно пользователяю
#         fields = ('title', 'cat_id')


# # Функция кодирует данные в JSON -> заменены на класс
# def encode():
#     '''Прогоняем объект model через сериализитор. То коллеция data представляет собой словарь.
#     Затем его пропускаем через json render, и получаем байтовую строку. Которую можно отдавать клиенту.
#     То есть объект -> словарь -> json-строка.'''
#     model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')
#     model_sr = WomenSerializer(model)  # Здесь отрабатывает сериализатор вместо атрибутов создаёт коллецию data
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)  # Преобразует объект серилизации в байтовую JSON строку
#     print(json, type(json), sep='\n')


# # Функция декодирует данные из JSON -> заменены на класс
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angelina Jolie"}')
#     data = JSONParser().parse(stream)  # Передаём весь поток парсеру
#     serializer = WomenSerializer(data=data)  # Преобразовываем, чтобы получить объект данных
#     serializer.is_valid()  # Проверка принятых данных на корректность
#     print(serializer.validated_data)
