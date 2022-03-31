import io

from rest_framework import serializers
from .models import Women
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class WomenSerializer(serializers.Serializer):

    '''Класс-сериализатор для модели women. С помощью которого преобразуем объекты моделей в словарь,
    а затем его в json строку с помощью json render.
    Посколько сериализаторы доджны так же обновлять, сохранять и удалять данные - создаим ещё методы'''

    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)  # Параметры только для чтения
    time_update = serializers.DateTimeField(read_only=True)  # Параметры только для чтения
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    '''Указав в методе только параметр validate_date - это метод create.
    Указав ещё и instance - это метод update.
    Вот там сериализатор сам понимает какой из метод вызывать.'''

    # Метод создания новой записи
    def create(self, validated_data):
        # Добавялем новую запись и возвращаем её
        return Women.objects.create(**validated_data)

    # Метод обновления старой записи
    def update(self, instance, validated_data):

        '''instance - ссылка на модель объекта women.
        validated_data - словарь данных для изменения'''

        # Берём ключ из словаря, и если его нету берём через из instance
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()  # Сохраняет запись в базе данных
        return instance  # Возвращает объект instance
