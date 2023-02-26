from rest_framework import routers

from .views import SongAPIViewSet

router = routers.SimpleRouter()
router.register(r"song", SongAPIViewSet)

urlpatterns = router.urls
