# Generated by Django 3.0.5 on 2020-04-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_managementsentials', '0010_auto_20200421_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='etage',
            field=models.IntegerField(choices=[(-1, '1. Untergeschoss'), (0, 'Erdgeschoss'), (1, '1. Etage'), (2, '2. Etage')]),
        ),
    ]