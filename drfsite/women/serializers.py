import io

from rest_framework import serializers
from .models import Women
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class WomenSerializer(serializers.ModelSerializer):

    '''Посколько сериализатор напрямую связан с таблицей Women, то есть более простая схема реализаци.
    Значительно упрощает текст программы'''

    class Meta:
        model = Women  # Модель Women
        # fields = ("title", "content", "cat")  # Какие поля из таблицы будем возвращать клинету
        fields = "__all__"  # Чтобы абсолютно все поля возвращалась обратно пользователю
