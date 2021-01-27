from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
from django.utils.translation import ugettext_lazy as _
from .validators import check_phone


class CustomUser(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(_('email address'), null=False, blank=False, unique=True)
    image = models.ImageField(upload_to=f'userImages/%Y/%m/%d/', null=True, blank=True)
    phone = models.CharField('شماره موبایل', max_length=11, validators=[check_phone], unique=True)

    def __str__(self):
        return self.username

class Tag(models.Model):
    tag_name = models.CharField('برچسب', max_length=20)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'

class Category(models.Model):
    category_name = models.CharField('دسته بندی', max_length=20)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Post(models.Model):
    post_title = models.CharField('عنوان', max_length=50)
    post_text = models.TextField('متن')
    post_image = models.ImageField(upload_to=f'postImages/%Y/%m/%d/', null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_show = models.BooleanField('نمایش', default=False)
    tag = models.ManyToManyField(Tag, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post_title} by {self.author.username}'

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'


class Comment(models.Model):
    comment_text = models.CharField('کامنت', max_length=300)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment written by {self.author.username}'

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.post and not self.comment:
            raise Exception('like must have refrence to a post or comment!')
        super(self, Like).save(*args, **kwargs)

    def __str__(self):
        return f'{self.post.post_title}{self.comment.comment_text} Liked by {self.user.username}'

    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'

class Dislike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.post and not self.comment:
            raise Exception('Dislike must have refrence to a post or comment!')
        super(self, Dislike).save(*args, **kwargs)

    def __str__(self):
        return f'{self.comment.comment_text}{self.post.post_title} Disliked by {self.user.username}'

    class Meta:
        verbose_name = 'دیسلایک'
        verbose_name_plural = 'دیسلایک ها'