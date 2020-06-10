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
    description = models.CharField(max_length=256, unique=True, primary_key=True)
    location = models.ForeignKey('Location', null=True, on_delete=models.SET_NULL, blank=True)
    blackboard = models.BooleanField(blank=True, null=True)
    chair = models.DecimalField(blank=True, max_digits=3, decimal_places=0, null=True)
    table = models.DecimalField(blank=True, max_digits=3, decimal_places=0, null=True)

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
    room = models.ForeignKey('Room', null=True, blank=True, on_delete=models.SET_NULL)
    serialnumber = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, unique=True, primary_key=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    date_of_purchase = models.DateTimeField(blank=True, null=True)
    warranty_period = models.IntegerField(blank=True, null=True)
    working = 'working'
    broken = 'broken'
    status_choice = [(working, "working"), (broken, "broken")]
    status = models.CharField(choices=status_choice, max_length=7, blank=True, null=True)

    class Meta:
        abstract = True


class Beamer(Device):
    HDMI = models.BooleanField(blank=True, null=True)
    VGA = models.BooleanField(blank=True, null=True)
    DVI = models.BooleanField(blank=True, null=True)
    DB = models.BooleanField(blank=True, null=True)
    USBTypeC = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return 'Beamer ' + self.description

    class Meta:
        verbose_name = "Beamer"
        verbose_name_plural = "Beamers"


class Computer(Device):
    def __str__(self):
        return 'Computer ' + self.description

    class Meta:
        verbose_name = "Computer"
        verbose_name_plural = "Computers"


class Screen(Device):
    format43 = '4:3'
    format169 = '16:9'
    format1610 = '16:10'
    format219 = '21:9'

    screen_format_choice = [(format43, '4:3'), (format169, '16:9'), (format1610, '16:10'),
                            (format219, '21:9')]
    screen_format = models.CharField(choices=screen_format_choice, max_length=5, blank=True, null=True)

    def __str__(self):

        return 'Screen ' + self.description

    class Meta:
        verbose_name = "Screen"
        verbose_name_plural = "Screens"


class SmartBoard(Device):
    def __str__(self):
        return 'SmartBoard ' + self.description

    class Meta:
        verbose_name = "SmartBoard"
        verbose_name_plural = "SmartsBoards"


class Canvas(Device):
    format11 = '1:1'
    format43 = '4:3'
    format169 = '16:9'
    format1610 = '16:10'
    format219 = '21:9'
    canvas_format_choice = [(format11, '1:1'), (format43, '4:3'), (format169, '16:9'), (format1610, '16:10'),
                            (format219, '21:9')]
    canvas_format = models.CharField(choices=canvas_format_choice, max_length=5, blank=True, null=True)

    def __str__(self):
        return 'Leinwand ' + self.description

    class Meta:
        verbose_name = "Canvas"
        verbose_name_plural = "Canvas"


class SpeakerSet(Device):
    quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return 'Audioanlage ' + self.description

    class Meta:
        verbose_name = "SpeakerSet"
        verbose_name_plural = "SpeakerSets"


