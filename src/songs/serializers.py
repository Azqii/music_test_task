from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    """Класс для сериализации модели Song"""
    record_author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Song
        fields = "__all__"
