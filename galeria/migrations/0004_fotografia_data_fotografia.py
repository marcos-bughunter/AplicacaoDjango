# Generated by Django 4.1 on 2023-01-14 20:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0003_fotografia_publicada"),
    ]

    operations = [
        migrations.AddField(
            model_name="fotografia",
            name="data_fotografia",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 1, 14, 17, 46, 42, 244433)
            ),
        ),
    ]