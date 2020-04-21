from django.db import models
from django.db import models


class Class(models.Model):
    etage = models.SmallIntegerField()
    class_number = models.SmallIntegerField()
    constructionphase = models.SmallIntegerField
    class_name = models.CharField(max_length=30)
