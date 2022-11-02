from django.shortcuts import render, get_object_or_404
from .models import Artiste, Song


# third party imports
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ArtisteSerializer, SongSerializer


class ArtisteListView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Artiste.objects.all()
        serializer = ArtisteSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArtisteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class SongListCreateView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SongRetrieveView(generics.RetrieveAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    lookup_field = 'pk'


@api_view(['GET', 'POST'])
def song_detail_view(request, pk=None, *args, **kwargs):
    if pk is not None:
        obj = get_object_or_404(Song, pk=pk)
        data = SongSerializer(obj, many=False).data
        return Response(data)


class SongUpdateView(generics.UpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'pk'


class SongDeleteView(generics.DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'pk'
