from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializer import PostSerializer
from myblog.models import Post


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer