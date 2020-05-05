from django.contrib import admin
from .models import Room, Beamer, Computer, Screen, Canvas, SmartBoard, SpeakerSet, Location, Brand

admin.site.register(Location)
admin.site.register(Room)
admin.site.register(Brand)
admin.site.register(Beamer)
admin.site.register(Computer)
admin.site.register(Screen)
admin.site.register(Canvas)
admin.site.register(SmartBoard)
admin.site.register(SpeakerSet)
# Register your models here.
