from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin, \
    DestroyModelMixin

from .models import Author, Album, Song
from .serializers import AuthorSerializer, AlbumSerializer, SongSerializer


class AuthorApi(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка авторов и создание нового автора."""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request):
        """Функция получения списка модели Авторов."""
        return self.list(request)

    def post(self, request, format=None):
        """Функция добавления Автора."""
        return self.create(request)


class DetailAuthorApi(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """Представление для получения детальной информации об авторе, а так же для редактирования и удаления объекта"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        """Функция получения детальной информации"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Функция редактирования объекта модели"""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Функция удаления объекта модели"""
        return self.destroy(request, *args, **kwargs)


class AlbumApi(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка альбома и создание нового альбома."""
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get(self, request):
        """Функция получения списка модели Альбом."""
        return self.list(request)

    def post(self, request, format=None):
        """Функция добавления Альбом."""
        return self.create(request)


class DetailAlbumApi(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """Представление для получения детальной информации об альбоме, а так же для редактирования и удаления объекта"""
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get(self, request, *args, **kwargs):
        """Функция получения детальной информации"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Функция редактирования объекта модели"""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Функция удаления объекта модели"""
        return self.destroy(request, *args, **kwargs)



class SongApi(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка песен и создание новой песни."""
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get(self, request):
        """Функция получения списка модели Песни."""
        return self.list(request)

    def post(self, request, format=None):
        """Функция добавления Песен."""
        return self.create(request)


class DetailSongApi(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """Представление для получения детальной информации об песне, а так же для редактирования и удаления объекта"""
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get(self, request, *args, **kwargs):
        """Функция получения детальной информации"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Функция редактирования объекта модели"""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Функция удаления объекта модели"""
        return self.destroy(request, *args, **kwargs)


