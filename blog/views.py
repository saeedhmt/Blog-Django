from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from blog.models import Post
from django.views import generic


# def index(request):
#     latest_posts = Post.objects.order_by('-datetime')[:5]
#     context = {'latest_posts' : latest_posts}
#     return render(request, 'blog/index.html', context= context)


class IndexListView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return Post.objects.filter(show=True).order_by('-datetime')[:5]