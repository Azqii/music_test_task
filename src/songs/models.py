from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Song(models.Model):
    """Модель песни"""
    record_author = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор записи")
    title = models.CharField(max_length=100, blank=False, verbose_name="Название")

    def __str__(self):
        return f"{self.title}"
