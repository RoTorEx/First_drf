from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):

    '''Собственный класс ограничения доступа. Чтобы читать могли все, а удалять только админмистратор'''

    def has_permission(self, request, view):
        # Если запрос безопасный (принадлежит запросам только для чтения: GET, HEAD, OPTIONS),
        # то предоставляем права доступа для всех
        if request.method in permissions.SAFE_METHODS:
            return True

        # Тут проверяем, что пользователь вошёл как администратор
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):

    '''Собсвтенный класс ограничения доступа на редактирование записей.'''

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Если пользователь из БД равен пользователю которы пришёл с запросом
        return obj.user == request.user


'''Устройство класса BasePermission'''
# class BasePermission(metaclass=BasePermissionMetaclass):
#     def has_permission(self, request, view):
#         return True

#     def has_object_permission(self, request, view, obj):
#         return True
