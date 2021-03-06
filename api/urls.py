from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path('tags/', views.tag_list, name='tag_list'),
    path('tags/<int:pk>/', views.tag_detail, name='tag_detail'),
    path('category/', views.category_list, name="category_list"),
    path('category/<int:pk>/', views.category_detail, name="category_detail"),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>', views.post_detail, name='post_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)