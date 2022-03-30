from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255)  # Заголовок
    content = models.TextField(blank=True)  # Описание женщик
    time_create = models.DateTimeField(auto_now_add=True)  # Время создание записи
    time_update = models.DateTimeField(auto_now=True)  # Время изменения записи
    is_published = models.BooleanField(default=True)  # Статус записи
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)  # Внешний ключи, ссылка на модель категори

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)  # Определяет что за категория женщины

    def __str__(self):
        return self.name
