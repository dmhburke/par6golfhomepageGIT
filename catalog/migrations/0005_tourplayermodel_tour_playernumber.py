# Generated by Django 2.2.7 on 2019-11-30 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20191120_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourplayermodel',
            name='tour_playernumber',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]