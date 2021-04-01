# Generated by Django 3.1.7 on 2021-03-25 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210322_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='isStarred',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mail',
            name='timeStamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='mail',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
