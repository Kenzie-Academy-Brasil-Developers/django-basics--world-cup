# Generated by Django 4.1.3 on 2022-11-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]
