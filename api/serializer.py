from rest_framework import serializers
from myblog.models import Post


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['title', 'author', 'body']