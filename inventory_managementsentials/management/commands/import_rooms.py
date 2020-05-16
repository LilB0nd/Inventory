from django.core.management.base import BaseCommand
#from polls.models import Question as Poll


class Command(BaseCommand):
    help = 'Imports rooms as a svg file'

    def handle(self, *args, **options):
        self.stdout.write("Import rooms")

