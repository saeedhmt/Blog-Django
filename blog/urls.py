from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('newpost/', views.new_post, name='newpost'),
    path('post_detail/<int:post_id>/', views.post_detail,name='post_detail'),
    # path('post_detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post_edit/<int:post_id>/', views.post_edit, name='post_edit'),
    path('comment_edit/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('categories/', views.categoties, name='categories'),
    path('category_posts/<int:category_id>/', views.category_posts, name='category_posts'),
]