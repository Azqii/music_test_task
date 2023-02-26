from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

from performers.models import Performer
from songs.models import Song


class Album(models.Model):
    """Модель альбома"""
    record_author = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор записи")
    title = models.CharField(max_length=100, blank=False, verbose_name="Название")
    release_date = models.DateField(verbose_name="Дата выпуска")
    performer = models.ForeignKey(
        to=Performer, on_delete=models.CASCADE, verbose_name="Исполнитель", related_name="albums"
    )

    def __str__(self):
        return f"{self.title}"


class AlbumSong(models.Model):
    """Модель песен в альбомах"""
    record_author = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор записи")
    album = models.ForeignKey(to=Album, on_delete=models.CASCADE, verbose_name="Альбом", related_name="songs")
    song = models.ForeignKey(to=Song, on_delete=models.CASCADE, verbose_name="Песня", related_name="albums")
    serial_number = models.IntegerField()

    class Meta:
        unique_together = ("album", "song")

    def __str__(self):
        return f"{self.album}| {self.serial_number}. {self.song}"

