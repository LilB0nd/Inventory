
from django.db import models


class Class(models.Model):

    etage_nr = [(-1, "1. Untergeschoss"),
                (0, "Erdgeschoss"),
                (1, "1. Etage"),
                (2, "2. Etage")]
    constructionsphase_nr = [(1, "Erster Bauabschnitt"), (2, "Zweiter Bauabschnitt")]

    etage = models.IntegerField(choices=etage_nr)
    classroom_ID = models.IntegerField(default=1)
    constructionphase = models.IntegerField(choices=constructionsphase_nr)
    chairs = models.IntegerField(default=1)
    table = models.IntegerField(default=1)

    def __str__(self):
        return "Klassenraumzimmer: " + str(self.classroom_ID)

    class Meta:
        verbose_name = "Klasseraum"
        verbose_name_plural = "Klassenräume"


class Beamer(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE, default=0)
    price = models.IntegerField()
    date_of_purchase = models.DateTimeField()
    serialnumber = models.IntegerField(default=1)
    warranty_period = models.IntegerField(default=1)
    status = [("working", "funktioniert"), ("broken", "kaputt")]
    status = models.CharField(choices=status, max_length=30)

    def __str__(self):
        return "Beamerseriennummer: " + str(self.serialnumber)

    class Meta:
        verbose_name = "Beamer"
        verbose_name_plural = "Beamer"
