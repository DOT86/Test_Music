from django.db import models

class Author(models.Model):
    """Модель Исполнитель."""
    name = models.CharField(max_length=100, default=None)

class Album(models.Model):
    """Модель Альбом."""
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='author')
    year = models.IntegerField(max_length=4, )

class Song(models.Model):
    """Модель Песня."""
    name = models.CharField(max_length=100, default=None)
    number = models.IntegerField(max_length=1000, unique=True)
    album = models.ForeignKey(Album, on_delete=models.PROTECT, related_name='album')


