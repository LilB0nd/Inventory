from django.db import models


class Location(models.Model):
    BASEMENT = 'BA'
    GROUNDFLOOR = 'GF'
    FIRSTFLOOR = 'FF'
    SECONDFLOOR = 'SF'
    FLOOR_IN_BUILDING_FLOOR_CHOICES = ((BASEMENT, 'Keller'), (GROUNDFLOOR, 'Erdgeschoss'), (FIRSTFLOOR, '1. Etage'),
                                       (SECONDFLOOR, '2. Etage'),
                                       )
    floor = models.CharField(
        max_length=2,
        choices=FLOOR_IN_BUILDING_FLOOR_CHOICES,
        default=FIRSTFLOOR
    )
    BUILDING1 = 'BA1',
    BUILDING2 = 'BA2',
    GYMNASIUM = 'GYM',
    BUILDING_IN_BUILDING_CHOICES = (
        ('BUILDING1', 'Erster Bauabschnitt'), ('BUILDING2', 'Zweiter Bauabschnitt'), ('GYMNASIUM', 'Sporthalle'),
    )
    building = models.CharField(max_length=9, choices=BUILDING_IN_BUILDING_CHOICES, default=BUILDING1)

    def __str__(self):
        return "{} / {}".format(self.get_floor_display(), self.get_building_display())


class Room(models.Model):
    description = models.CharField(max_length=256, primary_key=True)
    location = models.ForeignKey('Location', null=True, on_delete=models.SET_NULL, blank=True)
    beamer = models.OneToOneField('Beamer', null=True, on_delete=models.SET_NULL, blank=True)
    smartboard = models.OneToOneField('SmartBoard', null=True, on_delete=models.SET_NULL, blank=True)
    canvas = models.OneToOneField('Canvas', null=True, on_delete=models.SET_NULL, blank=True)
    speakerset = models.OneToOneField('SpeakerSet', null=True, on_delete=models.SET_NULL, blank=True)
    chair = models.DecimalField(blank=True, max_digits=3, decimal_places=0, null=True)
    table = models.DecimalField(blank=True, max_digits=3, decimal_places=0, null=True)
    blackboard = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "room"
        verbose_name_plural = "rooms"


class Brand(models.Model):
    description = models.CharField(max_length=256, null=True, unique=True)

    def __str__(self):
        return self.description


class Device(models.Model):
    serialnumber = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, primary_key=True, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    date_of_purchase = models.DateTimeField(blank=True, null=True)
    warranty_period = models.IntegerField(blank=True, null=True)
    status = [("working", "working"), ("broken", "broken")]
    status = models.CharField(choices=status, max_length=7, blank=True, null=True)

    class Meta:
        abstract = True


class Beamer(Device):
    def __str__(self):
        self.description = 'Beamer ' + self.description
        return self.description

    class Meta:
        verbose_name = "Beamer"
        verbose_name_plural = "Beamers"


class Computer(Device):
    room = models.ForeignKey('Room', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        self.description = 'Computer ' + self.description
        return self.description

    class Meta:
        verbose_name = "Computer"
        verbose_name_plural = "Computers"


class Screen(Device):
    room = models.ForeignKey('Room', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        self.description = 'Screen ' + self.description
        return self.description

    class Meta:
        verbose_name = "Screen"
        verbose_name_plural = "Screens"


class SmartBoard(Device):
    def __str__(self):
        self.description = 'SmartBoard ' + self.description
        return self.description

    class Meta:
        verbose_name = "SmartBoard"
        verbose_name_plural = "SmartsBoards"


class Canvas(Device):
    def __str__(self):
        self.description = 'Leinwand ' + self.description
        return self.description

    class Meta:
        verbose_name = "Canvas"
        verbose_name_plural = "Canvas"


class SpeakerSet(Device):
    quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        self.description = 'LautsprecherSet ' + self.description
        return self.description

    class Meta:
        verbose_name = "SpeakerSet"
        verbose_name_plural = "SpeakerSets"


