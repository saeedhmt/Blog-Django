from rest_framework import serializers
from blog.models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'get_count_posts']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'main_cat', 'get_count_posts']


class PostSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'image',
                  'show', 'datetime', 'active',
                  'get_count_likes', 'get_count_dislikes']

class PostSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'show', 'datetime',
                  'active', 'get_count_likes', 'get_count_dislikes']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'datetime', 'show',
                  'get_count_likes', 'get_count_dislikes']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'is_like', 'datetime']