from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


class WomenSerializer(serializers.ModelSerializer):

    '''Посколько сериализатор напрямую связан с таблицей Women, то есть более простая схема реализаци.
    Значительно упрощает текст программы'''

    # Связываемся с моделью women, а атрибут user заполняем через скрытое поле, где прописывается текущий пользователь
    # То есть при добавлении записи через API она будет связана именно с пользователем добавившим её
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women  # Модель Women
        # fields = ("title", "content", "cat")  # Какие поля из таблицы будем возвращать клинету
        fields = "__all__"  # Чтобы абсолютно все поля возвращалась обратно пользователю
