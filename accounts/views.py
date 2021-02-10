from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from blog.models import Post, Comment


@login_required
def profile(request):
    admin_group = Group.objects.get(name='مدیر')
    editor_group = Group.objects.get(name='ویراستار')

    if admin_group in request.user.groups.all() or editor_group in request.user.groups.all():
        return HttpResponseRedirect(reverse('admin:index'))

    else:
        user_id = request.user.id
        posts = Post.objects.filter(author_id=user_id)
        comments = Comment.objects.filter(author_id=user_id)
        context = {'posts' : posts, 'comments' : comments}

        return render(request, 'accounts/profile.html', context=context)

