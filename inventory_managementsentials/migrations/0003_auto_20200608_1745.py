# Generated by Django 3.0.5 on 2020-06-08 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_managementsentials', '0002_canvas_format'),
    ]

    operations = [
        migrations.RenameField(
            model_name='canvas',
            old_name='format',
            new_name='canvas_format',
        ),
        migrations.AddField(
            model_name='beamer',
            name='DB',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='beamer',
            name='DVI',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='beamer',
            name='HDMI',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='beamer',
            name='USBTypeC',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='beamer',
            name='VGA',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='blackboard',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='screen',
            name='screen_format',
            field=models.CharField(blank=True, choices=[('1:1', '1:1'), ('4:3', '4:3'), ('16:9', '16:9'), ('16:10', '16:10'), ('21:9', '21:9')], max_length=5, null=True),
        ),
    ]
