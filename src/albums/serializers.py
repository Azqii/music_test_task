from rest_framework import serializers

from .models import Album, AlbumSong


class AlbumSerializer(serializers.ModelSerializer):
    """Сериализатор для объектов класса Album"""
    record_author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Album
        fields = "__all__"


class AlbumSongSerializer(serializers.ModelSerializer):
    """Сериализатор для объектов класса AlbumSong"""
    record_author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = AlbumSong
        fields = "__all__"
