from rest_framework import viewsets
from .models import FaceEmbed
from .serializers import BookSerializer


class FaceEmbedViewSet(viewsets.ModelViewSet):
    queryset = FaceEmbed.objects.all()
    serializer_class = BookSerializer
