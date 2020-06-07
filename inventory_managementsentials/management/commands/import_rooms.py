from django.core.management.base import BaseCommand
from inventory_managementsentials.models import Room


class Command(BaseCommand):
    help = 'Imports rooms as a svg file'

    def handle(self, *args, **options):
        self.stdout.write("Import rooms")
        room_file = open("./inventory_managementsentials/management/commands/sql_raeume.csv")
        print(Room.objects.all())
        for line in room_file:
            room_number = line.split(',')[1]

            room = Room(description=room_number)
            room.save()

            self.stdout.write("Imported room : {}".format(room_number))
