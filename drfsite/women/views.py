from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer


class WomenAPIListPagination(PageNumberPagination):

    '''Собственный класс для пагинации'''

    page_size = 4  # Кол-во записей на странице
    page_size_query_param = 'page_size'  # Это дополнительный паматре для запроса, прописывается через & (?)
    max_page_size = 3  # Максимальное кол-во, сколько может вызвать записей клиент на странице


class WomenAPIList(generics.ListCreateAPIView):
    '''Возвращает запись'''
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # Строка запрещает редактиврование статей через API неавторизированным пользователям
    permission_classes = (IsAuthenticatedOrReadOnly, )
    # Указываем класс пагинации
    pagination_class = WomenAPIListPagination


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    '''Обновляет запись'''
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # Ссылаемся на собсвенный класс
    # permission_classes = (IsOwnerOrReadOnly, )
    # Строчки ниже в этом представлении будут предоставлять доступ только тем пользователям,
    # которые получают доступ по токенам, и по сессия ничего не получится получить
    authentication_classes = (TokenAuthentication, )
    # Закомментим эту строчку, чтобы всё работало по JWT
    # permission_classes = (IsAuthenticated, )


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    '''Удаляеть запись'''
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # Удалять записи может только администратор сайта, но тогда просматривать никто не сможет
    permission_classes = (IsAdminOrReadOnly, )
