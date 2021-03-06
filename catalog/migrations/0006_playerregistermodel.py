# Generated by Django 2.2.7 on 2019-12-04 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_tourplayermodel_tour_playernumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerRegisterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_status', models.CharField(blank=True, choices=[('', 'Select availability'), ('YES', 'Lock me in'), ('MAYBE', 'Keep me informed'), ('NO', 'Out')], max_length=30, null=True)),
                ('comments', models.CharField(blank=True, max_length=200, null=True)),
                ('player_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.PlayerModel')),
            ],
        ),
    ]
