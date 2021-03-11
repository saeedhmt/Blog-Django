from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views


app_name = 'api'

urlpatterns = [
    # path('tags/', views.tag_list, name='tag_list'),
    path('tags/', views.TagList.as_view(), name='tag_list'),
    # path('tags/<int:pk>/', views.tag_detail, name='tag_detail'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tag_detail'),
    # path('category/', views.category_list, name="category_list"),
    path('category/', views.CategoryList.as_view(), name='category_list'),
    # path('category/<int:pk>/', views.category_detail, name="category_detail"),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category_detail'),
    # path('posts/', views.post_list, name='post_list'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    # path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    # path('comments/', views.comment_list, name='comment_list'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    # path('comments/<int:pk>/', views.comment_detail, name='comment_detail'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment_detail'),
    # path('likes/', views.like_list, name='like_list'),
    path('likes/', views.LikeList.as_view(), name='like_list'),
    # path('likes/<int:pk>/', views.like_detail, name='like_detail'),
    path('likes/<int:pk>/', views.LikeDetail.as_view(), name='like_detail'),
    # path('users/', views.custom_user_list, name='user_list'),
    path('users/', views.CustomUserList.as_view(), name='user_list'),
    path('users/<int:pk>/', views.CustomUserDetail.as_view(), name='user_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)