"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from women.views import *
from rest_framework import routers


class MyCustomRouter(routers.SimpleRouter):

    '''Нащ кастомный класс-роутер'''

    routes = [
        routers.Route(url=r'^{prefix}$',  # Шаблон маршрута, адреса определны без обратного слеша
                      mapping={'get': 'list'},  # Связывает тип запроса с соответствующим методов ViewSet'а
                      name='{basename}-list',  # Название маршрута
                      detail=False,  # Список или запись
                      # Доп. аругменты передаётся конкретному определнию при срабатывании маршрута
                      initkwargs={'suffix': 'List'}),
        routers.Route(url=r'^{prefix}/{lookup}$',
                      mapping={'get': 'retrieve'},
                      name='{basename}-detail',
                      detail=True,
                      initkwargs={'suffix': 'Detail'})
    ]


# Следующая реализация создаёт объект роутера. Откуда мы обращаемся. Создаим простой роутер
'''У такого метода не существует этого маршрута: http://127.0.0.1:8000/api/v1/'''
# router = routers.SimpleRouter()  # Из ветки роутер мы обращаемся к классу симп роутер, создаим объект класса
'''А у такого метода такой маршрут: http://127.0.0.1:8000/api/v1/ существует'''
# router = routers.DefaultRouter()
router = MyCustomRouter()  # Свой роутер
# Первым аругментом идёт префикс для набора маршрута. Вторым указываем класс
router.register(r'women', WomenViewSet, basename='men')  # Можем задать свой префикс имени маршрута
# print(router.urls)

urlpatterns = [
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
    # Весь набор маршрутов которые сгенерированы роутером и сразу их подключаем
    path('admin/', admin.site.urls),
    # Этот маршрут отвечает и за получение (get) списка статей, и за добавление (post) новой записи
    # Если укажем ключ, например "/9/" - отобразится 9ая статья и её можно изменить (put) или удалить (delete)
    path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/women/
]
