from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .models import Scene,Word,Bookmark
from .serializers import SceneSerializer,WordSerializer,BookmarkSerializer
# Create your views here.

class SceneViewSet(viewsets.ModelViewSet):
    queryset = Scene.objects.all()
    serializer_class = SceneSerializer

class WordViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Word.objects.filter(scene=self.kwargs['pk'])
        else:
            return Word.objects.all()
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)
    


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request):
        user = request.user
        bookmarks = Bookmark.objects.all().filter(user=user.id)
        serializer = BookmarkSerializer(bookmarks,many=True)
        return Response(serializer.data)
    def create(self,request):
        user = request.user
        bookmark = Bookmark(user=user,word=request.data["word"],definition=request.data["definition"])
        bookmark.save()
        serializer = BookmarkSerializer(bookmark)
        return Response(serializer.data)



