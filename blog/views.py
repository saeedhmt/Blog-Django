from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.urls import reverse

from blog.forms import PostModelForm
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
        return Post.objects.filter(active=True).filter(show=True).order_by('-datetime')[:5]

@login_required
@permission_required('blog.add_post')
def new_post(request):
    if request.method == 'POST':
        form_post = PostModelForm(request.POST)

        if form_post.is_valid():
            post = form_post.save(commit=False)
            post.author = request.user
            post.save()
            form_post._save_m2m()

            return HttpResponseRedirect(reverse('blog:index'))

    else:
        form_post = PostModelForm()

    return render(request, 'blog/newpost.html', {'form_post' : form_post})