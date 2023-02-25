from .models import Album, AlbumSong


class AlbumRepository:
    """Репозиторий запросов к базе данных из модели Album"""

    @staticmethod
    def get_albums():
        return Album.objects.all()


class AlbumSongRepository:
    """Репозиторий запросов к базе данных из модели AlbumSong"""

    @staticmethod
    def get_songs_with_albums():
        return AlbumSong.objects.all()
