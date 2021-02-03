from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('newpost/', views.new_post, name='newpost'),
    path('post_detail/<int:post_id>/', views.post_detail,name='post_detail'),
    # path('post_detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
]