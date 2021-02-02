from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('newpost/', views.new_post, name='newpost'),
]