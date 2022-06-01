from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializer import PostSerializer
from myblog.models import Post


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class PostDetail(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer   

class PostRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer    