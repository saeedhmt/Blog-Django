from django.contrib.auth.models import Group
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Create Group'

    def add_arguments(self, parser):
        parser.add_argument('groups', nargs='+', type=str)

    def handle(self, *args, **options):
        for group in options['groups']:
            Group.objects.create(name=group)
        self.stdout.write(self.style.SUCCESS('Groups created!'))
