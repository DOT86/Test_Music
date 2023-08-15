from rest_framework import serializers
from .models import Author, Album, Song





class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['author', 'year']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['number', 'name', 'album']