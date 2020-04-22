from django.db import models
# stift für smartboard
# bildschirme extra


class Class(models.Model):
    classroom_number = models.IntegerField(primary_key=True)
    etage_nr = [(-1, "1. basement"),
                (0, "ground level"),
                (1, "1. floor"),
                (2, "2. floor")]
    constructionsphase_nr = [(1, "First Constructionphase"), (2, "Second Constructionphase")]
    etage = models.IntegerField(choices=etage_nr)

    constructionphase = models.IntegerField(choices=constructionsphase_nr)

    def __str__(self):
        return str(self.classroom_number)

    class Meta:
        verbose_name = "classroom"
        verbose_name_plural = "classrooms"


class Beamer(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE, default=0)
    BeamerID = models.IntegerField(default=0, primary_key=True)
    serialnumber = models.CharField(max_length=256, blank=True, null=True)
    brand = models.CharField(max_length=256, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    date_of_purchase = models.DateTimeField(blank=True, null=True)
    warranty_period = models.IntegerField(blank=True, null=True)
    status = [("working", "working"), ("broken", "broken")]
    status = models.CharField(choices=status, max_length=7, blank=True, null=True)

    def __str__(self):
        return str(self.BeamerID)

    class Meta:
        verbose_name = "Beamer"
        verbose_name_plural = "Beamers"


class Computer(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE, default=0)
    ComputerID = models.IntegerField(default=0, primary_key=True)
    serialnumber = models.CharField(max_length=256, blank=True, null=True)
    brand = models.CharField(max_length=256, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    date_of_purchase = models.DateTimeField(blank=True, null=True)
    warranty_period = models.IntegerField(blank=True, null=True)
    status = [("working", "working"), ("broken", "broken")]
    status = models.CharField(choices=status, max_length=7, blank=True, null=True)

    def __str__(self):
        return str(self.ComputerID)

    class Meta:
        verbose_name = "Computer"
        verbose_name_plural = "Computers"


class Screen(models.Model):
    Computer = models.ForeignKey(Computer, on_delete=models.CASCADE, default=0)
    ScreenID = models.IntegerField(default=0, primary_key=True)
    serialnumber = models.CharField(max_length=256, blank=True, null=True)
    brand = models.CharField(max_length=256, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    date_of_purchase = models.DateTimeField(blank=True, null=True)
    warranty_period = models.IntegerField(blank=True, null=True)
    status = [("working", "working"), ("broken", "broken")]
    status = models.CharField(choices=status, max_length=7, blank=True, null=True)

    def __str__(self):
        return str(self.ScreenID)

    class Meta:
        verbose_name = "Screen"
        verbose_name_plural = "Screens"


class SmartBoard(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE, default=0)
    SmartBoardID = models.IntegerField(default=0, primary_key=True)
    serialnumber = models.CharField(max_length=256, blank=True, null=True)
    brand = models.CharField(max_length=256, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    date_of_purchase = models.DateTimeField(blank=True, null=True)
    warranty_period = models.IntegerField(blank=True, null=True)
    status = [("working", "working"), ("broken", "broken")]
    status = models.CharField(choices=status, max_length=7, blank=True, null=True)

    def __str__(self):
        return str(self.SmartBoardID)

    class Meta:
        verbose_name = "SmartBoard"
        verbose_name_plural = "SmartsBoards"


class Canvas(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE, default=0)
    CanvasID = models.IntegerField(default=0, primary_key=True)
    serialnumber = models.CharField(max_length=256, blank=True, null=True)
    brand = models.CharField(max_length=256, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    date_of_purchase = models.DateTimeField(blank=True, null=True)
    warranty_period = models.IntegerField(default=2, blank=True, null=True)
    status = [("working", "working"), ("broken", "broken")]
    status = models.CharField(choices=status, max_length=30, blank=True, null=True)

    def __str__(self):
        return str(self.CanvasID)

    class Meta:
        verbose_name = "Canvas"
        verbose_name_plural = "Canvas"


class SpeakerSet(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE, default=0)
    SpeakerSetID = models.IntegerField(default=0, primary_key=True)
    quantity = models.IntegerField(blank=True, null=True)
    brand = models.CharField(max_length=256, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    date_of_purchase = models.DateTimeField()
    warranty_period = models.IntegerField(blank=True, null=True)
    status = [("working", "working"), ("broken", "broken")]
    status = models.CharField(choices=status, max_length=30, blank=True, null=True)

    def __str__(self):
        return str(self.SpeakerSetID)

    class Meta:
        verbose_name = "SpeakerSet"
        verbose_name_plural = "SpeakerSets"
