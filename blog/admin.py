from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(CustomUser)
# admin.site.register(Post)
# admin.site.register(Comment)
# admin.site.register(Like)
# admin.site.register(Dislike)
# admin.site.register(Category)
# admin.site.register(Tag)

class PostInline(admin.StackedInline):
    model = Post

class CommentInline(admin.StackedInline):
    model = Comment

class LikeInline(admin.StackedInline):
    model = Like


class TagPostInline(admin.TabularInline):
    model = Post.tag.through



@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ('Info', {'fields' : ['image', 'first_name', 'last_name']})
    # ]
    fields = ('image', 'username', 'first_name', 'last_name', 'email', 'phone')
    inlines = (PostInline, CommentInline, LikeInline)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post', {'fields' : ('datetime', 'category','author', 'title', 'text', 'image', 'tag', 'show')}),
    ]
    # fields = ('category','author', 'title', 'text', 'image', 'tag', 'datetime', 'show')

    inlines = (CommentInline, LikeInline, TagPostInline)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('author', 'text', 'datetime', 'post')

    inlines = (LikeInline,)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    fields = ('user', 'post', 'comment', 'datetime', 'is_like')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ('name',)
    # filter_horizontal = (Post,)
    inlines = (TagPostInline,)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (PostInline,)