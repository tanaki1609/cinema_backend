from rest_framework import serializers
from .models import Film


class FilmListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'text', 'rating', 'is_hit']
        # fields = 'id title rating is_hit'.split()
        # fields = '__all__'
        # exclude = 'id created'.split()
