from rest_framework import serializers

from .models import Performer


class PerformerSerializer(serializers.ModelSerializer):
    """Класс для сериализации объектов модели Performer"""
    record_author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Performer
        fields = "__all__"
