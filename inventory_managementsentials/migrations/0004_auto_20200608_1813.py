# Generated by Django 3.0.5 on 2020-06-08 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_managementsentials', '0003_auto_20200608_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='screen_format',
            field=models.CharField(blank=True, choices=[('4:3', '4:3'), ('16:9', '16:9'), ('16:10', '16:10'), ('21:9', '21:9')], max_length=5, null=True),
        ),
    ]
