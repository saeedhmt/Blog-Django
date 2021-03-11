from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins
from blog.models import *
from blog.serializers import *
# Create your views here.


# @api_view(['GET', 'POST'])
# # def custom_user_list(request, format=None):
# #     """
# #     list all users or create one.
# #     """
# #     if request.method == 'GET':
# #         users = CustomUser.objects.all()
# #         serializer = CustomUserSerializer(users, many=True)
# #         return Response(serializer.data)
# #
# #     elif request.method == 'POST':
# #         serializer = CustomUserSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #
# #
# # class CustomUserList(mixins.ListModelMixin,
# #                      mixins.CreateModelMixin,
# #                      generics.GenericAPIView):
# #     queryset = CustomUser.objects.all()
# #     serializer_class = CustomUserSerializer
# #
# #     def get(self, request, *args, **kwargs):
# #         return self.list(request, *args, **kwargs)
# #
# #     def post(self, request, *args, **kwargs):
# #         return self.create(request, *args, **kwargs)


class CustomUserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# @api_view(['GET', 'PUT', 'DELETE'])
# def custom_user_detail(request, pk, format=None):
#     '''
#     Retrieve or update or delete a user.
#     '''
#     try:
#         user = CustomUser.objects.get(pk=pk)
#     except CustomUser.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = CustomUserSerializer(user)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = CustomUserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class CustomUserDetail(mixins.RetrieveModelMixin,
#                        mixins.UpdateModelMixin,
#                        mixins.DestroyModelMixin,
#                        generics.GenericAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUser
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

class CustomUserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# @api_view(['GET', 'POST'])
# def tag_list(request, format=None):
#     """
#     List all tags or create one.
#     """
#     if request.method == 'GET':
#         tags = Tag.objects.all()
#         serializer = TagSerializer(tags, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = TagSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             # print(type(serializer.data))
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# @api_view(['GET', 'PUT', 'DELETE'])
# def tag_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a tag.
#     """
#     try:
#         tag = Tag.objects.get(pk=pk)
#     except Tag.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = TagSerializer(tag)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'PUT':
#         serializer = TagSerializer(tag, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         tag.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# @api_view(['GET', 'POST'])
# def category_list(request, format=None):
#     """
#     List all categories or create one.
#     """
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# @api_view(['GET', 'PUT', 'DELETE'])
# def category_detail(request, pk, format=None):
#     """
#     Retreive, update of delete a category.
#     """
#     try:
#         category = Category.objects.get(pk=pk)
#     except Category.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#
#     elif request.method == "PUT":
#         serializer = CategorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "DELETE":
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# @api_view(['GET', 'POST'])
# def post_list(request, format=None):
#     """
#     List all posts or create one.
#     """
#
#     if request.method == "GET":
#         posts = Post.objects.all()
#         serializer = PostSerializerList(posts, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = PostSerializerList(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# @api_view(['GET', 'PUT', 'DELETE'])
# def post_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a post.
#     """
#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = PostSerializerDetail(post)
#         return Response(serializer.data)
#
#     elif request.method == "PUT":
#         serializer = PostSerializerDetail(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "DELETE":
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

# @api_view(['GET', 'POST'])
# def comment_list(request, format=None):
#     """
#     list all comments or create one.
#     """
#     if request.method == 'GET':
#         comments = Comment.objects.all()
#         serializer = CommentSerializerList(comments, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = CommentSerializerList(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# @api_view(['GET', 'PUT', 'DELETE'])
# def comment_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a comment.
#     """
#     try:
#         comment = Comment.objects.get(pk=pk)
#     except Comment.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = CommentSerializerDetail(comment)
#         return Response(serializer.data)
#
#     elif request.method == "PUT":
#         serializer = CommentSerializerDetail(comment, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "DELETE":
#         comment.delete()
#         return Response(status=status.HTTP_404_NOT_FOUND)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


# @api_view(['GET', 'POST'])
# def like_list(request, format=None):
#     """
#     list all likes or create one.
#     """
#
#     if request.method == "GET":
#         likes = Like.objects.all()
#         serializer = LikeSerializer(likes, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = LikeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# @api_view(['GET', "PUT", 'DELETE'])
# def like_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a like.
#     """
#     try:
#         like = Like.objects.get(pk=pk)
#     except Like.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = LikeSerializer(like)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = LikeSerializer(like, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         like.delete()
#         return Response(status=status.HTTP_404_NOT_FOUND)


class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)