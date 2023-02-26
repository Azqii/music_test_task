from .models import Performer


class PerformerRepository:
    """Репозиторий запросов к базе данных из модели Performer"""

    @staticmethod
    def get_performers():
        return Performer.objects.all()
