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

# Следующая реализация создаёт объект роутера. Откуда мы обращаемся. Создаим простой роутер
router = routers.SimpleRouter()  # Из ветки роутер мы обращаемся к классу симп роутер, создаим объект класса
router.register(r'women', WomenViewSet)  # Первым аругментом идёт префикс для набора маршрута. Вторым указываем класс

urlpatterns = [
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
    # Весь набор маршрутов которые сгенерированы роутером и сразу их подключаем
    path('admin/', admin.site.urls),
    # Этот маршрут отвечает и за получение (get) списка статей, и за добавление (post) новой записи
    # Если укажем ключ, например "/9/" - отобразится 9ая статья и её можно изменить (put) или удалить (delete)
    path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/women/
]
