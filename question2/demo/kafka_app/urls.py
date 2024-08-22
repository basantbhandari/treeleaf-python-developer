from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FaceEmbedViewSet

router = DefaultRouter()
router.register(r'face_embed', FaceEmbedViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
