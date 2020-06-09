from django.core.management.base import BaseCommand
from inventory_managementessentials.models import Room
class Command(BaseCommand):
    help = 'Importing rooms with Csv file'

    def handle(self, *args, **options):
            self.stdout.write("Import Rooms")
            self.stdout.write("There are {} rooms".format(Room.objects.count()))
            room_file = open('./inventory_managementessentials/management/commands/sql_raeume.csv', 'rt')
            for line in room_file:
                room_number = line.split(',')[1].strip()
                try:
                    existing_room = Room.objects.get(class_id=room_number)
                    self.stdout.write("{} Does already exist".format(room_number))
                except: Room.DoesNotExist
                room=Room(class_id=room_number)
                room.save()
                self.stdout.write("Imported room : {}".format(room_number))
