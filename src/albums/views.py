from rest_framework import generics, viewsets

from .serializers import AlbumSerializer, AlbumSongSerializer
from .repository import AlbumRepository, AlbumSongRepository


class AlbumListCreateAPIView(generics.ListCreateAPIView):
    """View для просмотра списка и создания записей в базе данных, соответствующих объектам класса Album"""
    queryset = AlbumRepository.get_albums()
    serializer_class = AlbumSerializer


class AlbumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """View для просмотра, изменения и удаления записей из базы данных, которые соответствуют объектам класса Album"""
    queryset = AlbumRepository.get_albums()
    serializer_class = AlbumSerializer


class AlbumSongAPIViewSet(viewsets.ModelViewSet):
    """ViewSet для всех CRUD операций с записями в базе данных, соответствующим объектам класса AlbumSong"""
    queryset = AlbumSongRepository.get_songs_with_albums()
    serializer_class = AlbumSongSerializer
