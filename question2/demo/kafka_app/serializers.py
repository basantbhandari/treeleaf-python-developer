from rest_framework import serializers
from .models import FaceEmbed


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceEmbed
        fields = '__all__'
