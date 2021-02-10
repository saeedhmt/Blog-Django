from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.urls import reverse

from blog.forms import PostModelForm, CommentModelForm
from blog.models import *
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


def categoty(request):
    categories = Category.objects.all()
    context = {'categories' : categories}
    return render(request, 'blog/categories.html', context=context)


def category_posts(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(category=category)
    context = {'posts' : posts, 'category' : category}
    return render(request, 'blog/category_posts.html', context=context)

# @login_required
@permission_required('blog.add_post')
def new_post(request):
    if request.method == 'POST':
        form_post = PostModelForm(request.POST)

        if form_post.is_valid():
            post = form_post.save(commit=False)
            post.author = request.user
            post.save()
            form_post.save_m2m()

            return HttpResponseRedirect(reverse('blog:index'))

    else:
        form_post = PostModelForm()

    return render(request, 'blog/newpost.html', {'form_post' : form_post})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    context = {'post' : post, 'comments' : comments}
    return render(request, 'blog/post_detail.html', context=context)

# class PostDetailView(generic.DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'


@permission_required('blog.change_post')
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form_post = PostModelForm(request.POST, instance=post)

        if form_post.is_valid():
            edited_post = form_post.save(commit=False)
            edited_post.author = request.user
            edited_post.save()
            form_post.save_m2m()

            return HttpResponseRedirect(reverse('profile'))

    else:
        form_post = PostModelForm(instance=post)
    return render(request, 'blog/post_edit.html',
                  {'form_post' : form_post, 'post' : post})


def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form_comment = CommentModelForm(request.POST, instance=comment)
        if form_comment.is_valid():
            edited_comment = form_comment.save(commit=False)
            edited_comment.author = request.user
            edited_comment.save()

            return HttpResponseRedirect(reverse('profile'))

    else:
        form_comment = CommentModelForm(instance=comment)
    return render(request, 'blog/comment_edit.html',
                  {'form_comment' : form_comment, 'comment' : comment})

