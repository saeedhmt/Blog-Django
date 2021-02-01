from django.contrib.auth.models import User, AbstractUser
from django.core.exceptions import FieldError, ValidationError
from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
# from django.utils.translation import ugettext_lazy as _
from .validators import check_phone


class CustomUser(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField('آدرس ایمیل', null=False, blank=False, unique=True)
    image = models.ImageField(upload_to=f'userImages/%Y/%m/%d/', null=True, blank=True)
    phone = models.CharField('شماره موبایل', max_length=11, validators=[check_phone], unique=True)
    datetime = models.DateTimeField('زمان و تاریخ ثبت نام کاربر', null=True, blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.datetime = timezone.now()
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField('برچسب', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'

    def get_count_posts(self):
        return self.post_set.count()

    get_count_posts.short_description = 'تعداد پست ها'


class Category(models.Model):
    name = models.CharField('دسته بندی', max_length=20)

    def get_count_posts(self):
        return self.post_set.count()

    get_count_posts.short_description = 'تعداد پست ها'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Post(models.Model):
    title = models.CharField('عنوان', max_length=50)
    text = models.TextField('متن')
    image = models.ImageField(upload_to=f'postImages/%Y/%m/%d/', null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    show = models.BooleanField('نمایش', default=False)
    tag = models.ManyToManyField(Tag, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    datetime = models.DateTimeField('زمان و تاریخ پست', null=True, blank=True)

    def get_tags(self):
        return ", ".join([tag.name for tag in self.tag.all()])

    get_tags.short_description = 'تگ ها'

    def __str__(self):
        return f'{self.title} by {self.author.username}'

    def save(self, *args, **kwargs):
        self.datetime = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'


class Comment(models.Model):
    text = models.TextField('کامنت', max_length=300)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    datetime = models.DateTimeField('زمان و تاریخ کامنت', null=True, blank=True)

    def __str__(self):
        return f'Comment written by {self.author.username}'

    def save(self, *args, **kwargs):
        self.datetime = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

class Like(models.Model):
    is_like = models.BooleanField('لایک', default=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    datetime = models.DateTimeField('زمان و تاریخ لایک', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.post and not self.comment:
            raise FieldError('like or dislike must have refrence to a post or comment!')
        elif self.post and self.comment:
            raise ValidationError('like or dislike must have refrence to a post or comment!')

        self.datetime = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.is_like:
            if self.post:
                return f'{self.post.title} Liked by {self.user.username}'
            else:
                return f'{self.comment.text} Liked by {self.user.username}'
        else:
            if self.post:
                return f'{self.post.title} Disliked by {self.user.username}'
            else:
                return f'{self.comment.text} Disliked by {self.user.username}'


    class Meta:
        verbose_name = 'لایک و دیسلایک'
        verbose_name_plural = 'لایک ها و دیسلایک ها'

# class Dislike(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#
#     def save(self, *args, **kwargs):
#         if not self.post and not self.comment:
#             raise FieldError('Dislike must have refrence to a post or comment!')
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return f'{self.comment.comment_text}{self.post.post_title} Disliked by {self.user.username}'
#
#     class Meta:
#         verbose_name = 'دیسلایک'
#         verbose_name_plural = 'دیسلایک ها'