from rest_framework import viewsets

from .repository import SongRepository
from .serializers import SongSerializer


class SongAPIViewSet(viewsets.ModelViewSet):
    """ViewSet модели песен"""
    queryset = SongRepository.get_songs()
    serializer_class = SongSerializer
