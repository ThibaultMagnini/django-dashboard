# Generated by Django 3.0.2 on 2020-01-14 20:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200114_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(default=datetime.date(2020, 1, 14)),
        ),
        migrations.AddField(
            model_name='profile',
            name='discordtag',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='game',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='ingame_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='region',
            field=models.CharField(blank=True, default='NA', max_length=3),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
    ]
