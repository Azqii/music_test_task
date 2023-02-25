from .models import Song


class SongRepository:
    """Репозиторий запросов к базе данных из модели Song"""
    @staticmethod
    def get_songs():
        return Song.objects.all()
