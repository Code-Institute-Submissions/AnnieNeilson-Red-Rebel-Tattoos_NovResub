# Generated by Django 3.2.14 on 2022-07-06 13:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='caption',
            field=models.CharField(default=datetime.datetime(2022, 7, 6, 13, 36, 50, 321876, tzinfo=utc), max_length=100, unique=True),
            preserve_default=False,
        ),
    ]