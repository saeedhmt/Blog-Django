from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.utils.translation import ngettext

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
    classes = ['collapse']


class CommentInline(admin.StackedInline):
    model = Comment
    classes = ['collapse']


class LikeInline(admin.TabularInline):
    model = Like
    classes = ['collapse']


class TagPostInline(admin.TabularInline):
    model = Post.tag.through
    classes = ['collapse']




# @admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # fieldsets = [
    #     ('Info', {'fields' : ['image', 'first_name', 'last_name']})
    # ]
    fieldsets = (
      ('اطلاعات کاربری', {'fields': ('username', 'email', 'password')}),
      ('اطلاعات شخصی', {'fields': ('image', 'image_tag', 'first_name',
                                    'last_name', 'phone', 'datetime')}),
      ('اجازه های کاربر', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions')}),
  )

    inlines = (PostInline, CommentInline, LikeInline)
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'username')
    readonly_fields = ('image_tag',)

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post', {'fields' : ('datetime', 'category','author', 'title',
                              'text', 'image', 'tag', 'show', 'active'),
                  }),
    ]
    # fields = ('category','author', 'title', 'text', 'image', 'tag', 'datetime', 'show')

    inlines = (CommentInline, LikeInline, TagPostInline)
    list_display = ('title', 'author', 'category', 'get_tags',
                    'datetime', 'show', 'active', 'get_count_likes',
                    'get_count_dislikes')
    list_filter = ('author', 'category', 'show','active', 'tag', 'datetime')
    search_fields = ('author', 'tag', 'category', 'title')

    def show_posts(self, request, queryset):
        updated = queryset.update(show=True)
        self.message_user(request, f'{updated} پست نمایش داده می شود.', messages.SUCCESS)

    show_posts.short_description = 'نمایش پست ها'

    def dont_show_posts(self, request, queryset):
        updated = queryset.update(show=False)
        self.message_user(request, f'{updated} پست نمایش داده نمی شود.', messages.ERROR)

    dont_show_posts.short_description = 'عدم نمایش پست ها'

    def active_posts(self, request, queryset):
        updated = queryset.update(active=True)
        self.message_user(request, f'{updated} پست فعال شد.', messages.SUCCESS)

    active_posts.short_description = 'فعال کردن پست ها'

    def deactive_posts(self, request, queryset):
        updated = queryset.update(active=False)
        self.message_user(request, f'{updated} پست غیرفعال شدند.', messages.ERROR)

    deactive_posts.short_description = 'غیرفعال کردن پست ها'

    actions = (show_posts, dont_show_posts, active_posts, deactive_posts)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('author', 'text', 'datetime', 'post', 'show')

    inlines = (LikeInline,)
    list_display = ('author', 'post', 'datetime', 'show',
                    'get_count_likes', 'get_count_dislikes')
    list_filter = ('author', 'datetime', 'post', 'show')
    search_fields = ('author', 'post')

    def show_comments(self, request, queryset):
        updated = queryset.update(show=True)
        self.message_user(request, f'{updated} نظر نمایش داده می شود.', messages.SUCCESS)

    show_comments.short_description = 'نمایش نظر ها'

    def dont_show_comments(self, request, queryset):
        updated = queryset.update(show=False)
        self.message_user(request, f'{updated} نظر نمایش داده نمی شود.', messages.ERROR)

    dont_show_comments.short_description = 'عدم نمایش نظر ها'
    actions = (show_comments, dont_show_comments)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    fields = ('user', 'post', 'comment', 'datetime', 'is_like')
    list_display = ('user', 'post', 'comment', 'datetime', 'is_like')
    list_filter = ('user', 'post', 'comment', 'datetime', 'is_like')
    search_fields = ('user', 'comment', 'post')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ('name',)
    inlines = (TagPostInline,)
    list_display = ('name', 'get_count_posts')
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'main_cat')
    inlines = (PostInline,)
    list_display = ('name', 'get_count_posts')
    search_fields = ('name',)