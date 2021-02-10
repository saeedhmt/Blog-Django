from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        groups = ['کاربر ساده', 'نویسنده', 'ویراستار', 'مدیر']
        user_group = Group.objects.create(name=groups[0])
        author_group = Group.objects.create(name=groups[1])
        editor_group = Group.objects.create(name=groups[2])
        admin_group = Group.objects.create(name=groups[3])

        default_perms = Permission.objects.filter(content_type__app_label='blog',
                                                     content_type__model__in=['post', 'comment', 'category'],
                                                     codename__contains='view')

        user_perms = Permission.objects.filter(content_type__app_label='blog',
                                               content_type__model__in=['comment', 'like'],
                                               codename__contains='add')

        author_perms = Permission.objects.filter(content_type__app_label='blog',
                                                 content_type__model__in=['post', 'tag'],
                                                 codename__in=['add_post', 'change_post',
                                                               'add_tag', 'change_tag'])

        editor_perms = Permission.objects.filter(content_type__app_label='blog',
                                                 content_type__model__in=['comment', 'post'],
                                                 codename__in=['add_comment', 'change_comment',
                                                               'add_post', 'change_post'])

        admin_perms = Permission.objects.all()

        for perm in default_perms:
            user_group.permissions.add(perm)
            author_group.permissions.add(perm)
            editor_group.permissions.add(perm)

        for perm in user_perms:
            user_group.permissions.add(perm)
            author_group.permissions.add(perm)
            editor_group.permissions.add(perm)

        for perm in author_perms:
            author_group.permissions.add(perm)
            editor_group.permissions.add(perm)

        for perm in editor_perms:
            editor_group.permissions.add(perm)

        for perm in admin_perms:
            admin_group.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS('Groups with permissions created!'))

