from rest_framework import serializers

from .models import Artiste, Song


class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = (
            'first_name', 'last_name',
            'age', 'song'
        )


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = (
            "title", 'released_date',
            'artiste_id', 'likes', 'lyric'
        )
