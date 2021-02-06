from django.contrib.auth.models import Group
from django.core.management import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Create Group'

    def add_arguments(self, parser):
        parser.add_argument('--create', nargs='+', type=str)
        parser.add_argument('--delete', nargs='+', type=str)

    def handle(self, *args, **options):
        # print(options['create'])
        # print(options['delete'])

        if options['create']:
            for group in options['create']:
                try:
                    Group.objects.create(name=group)
                except:
                    raise CommandError(f'Group {group} exists.')
            self.stdout.write(self.style.SUCCESS('Groups created!'))

        if options['delete']:
            for group in options['delete']:
                try:
                    Group.objects.get(name=group).delete()
                except Group.DoesNotExist:
                    raise CommandError(f'Group {group} does not exist.')
            self.stdout.write(self.style.ERROR('Groups deleted'))



