from rest_framework import viewsets

from .serializers import PerformerSerializer
from .repository import PerformerRepository


class PerformerAPIViewSet(viewsets.ModelViewSet):
    """View для CRUD операций с моделью Performer"""
    queryset = PerformerRepository.get_performers()
    serializer_class = PerformerSerializer
