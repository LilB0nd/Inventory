# Generated by Django 3.0.5 on 2020-06-10 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_managementsentials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beamer',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory_managementsentials.Room'),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory_managementsentials.Room'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory_managementsentials.Room'),
        ),
        migrations.AlterField(
            model_name='screen',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory_managementsentials.Room'),
        ),
        migrations.AlterField(
            model_name='smartboard',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory_managementsentials.Room'),
        ),
        migrations.AlterField(
            model_name='speakerset',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory_managementsentials.Room'),
        ),
    ]
