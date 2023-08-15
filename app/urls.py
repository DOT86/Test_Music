from django.urls import path
from .api import AlbumApi, DetailAlbumApi, AuthorApi, DetailAuthorApi, SongApi, DetailSongApi


urlpatterns = [
    path('author/', AuthorApi.as_view(), name='api_author'),
    path('author/<int:pk>/', DetailAuthorApi.as_view(), name='api_author_detail'),
    path('album/', AlbumApi.as_view(), name='api_album'),
    path('album/<int:pk>/', DetailAlbumApi.as_view(), name='api_album_detail'),
    path('song/', SongApi.as_view(), name='api_song'),
    path('song/<int:pk>/', DetailSongApi.as_view(), name='api_song_detail'),

]
