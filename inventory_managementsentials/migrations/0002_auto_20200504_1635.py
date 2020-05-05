# Generated by Django 3.0.5 on 2020-05-04 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_managementsentials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beamer',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory_managementsentials.Brand'),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory_managementsentials.Brand'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory_managementsentials.Brand'),
        ),
        migrations.AlterField(
            model_name='screen',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory_managementsentials.Brand'),
        ),
        migrations.AlterField(
            model_name='smartboard',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory_managementsentials.Brand'),
        ),
        migrations.AlterField(
            model_name='speakerset',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory_managementsentials.Brand'),
        ),
    ]
