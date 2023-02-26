from django.urls import path

from .views import PerformerAPIViewSet

urlpatterns = [
    path("performer/", PerformerAPIViewSet.as_view({"get": "list", "post": "create"})),
    path("performer/<int:pk>/", PerformerAPIViewSet.as_view({
        "get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"
    }))
]