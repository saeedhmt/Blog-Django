from rest_framework import serializers
from blog.models import *


class CustomUserSerializer(serializers.ModelSerializer):
    post_set = serializers.StringRelatedField(many=True)
    comment_set = serializers.StringRelatedField(many=True)
    like_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name',
                  'email', 'image', 'phone', 'datetime',
                  'post_set', 'comment_set', 'like_set']


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name', 'get_count_posts']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'main_cat', 'get_count_posts']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'image', 'author',
                  'show', 'datetime', 'active',
                  'get_count_likes', 'get_count_dislikes']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'text', 'datetime', 'show', 'author',
                  'get_count_likes', 'get_count_dislikes']


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        fields = ['id', 'user', 'is_like', 'datetime']