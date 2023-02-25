from django.urls import path
from rest_framework import routers

from .views import AlbumDetailAPIView, AlbumListCreateAPIView, AlbumSongAPIViewSet

router = routers.SimpleRouter()
router.register(r"album-song", AlbumSongAPIViewSet)

urlpatterns = [
    path("album/", AlbumListCreateAPIView.as_view(), name="album"),
    path("album/<int:pk>/", AlbumDetailAPIView.as_view(), name="album_detail")
] + router.urls
