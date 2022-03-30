from rest_framework import serializers
from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    '''Наследуется от серелизатора, который работает с моделями'''
    class Meta:
        model = Women
        # Ниже приведены поля для серилизации, то есть те, 
        # котрые будут отправляться обратно пользователяю
        fields = ('title', 'cat_id')
