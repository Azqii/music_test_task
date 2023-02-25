from rest_framework import routers

from .views import SongViewSet

router = routers.SimpleRouter()
router.register(r"song", SongViewSet)

urlpatterns = router.urls
