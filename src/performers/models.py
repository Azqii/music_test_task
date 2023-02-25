from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Performer(models.Model):
    """Модель исполнителя"""
    record_author = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор записи")
    name = models.CharField(max_length=100, blank=False, verbose_name="Имя")

    def __str__(self):
        return f"{self.name}"
