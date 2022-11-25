# Generated by Django 4.1.3 on 2022-11-25 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0003_remove_team_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="fifa_code",
            field=models.CharField(max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name="team",
            name="titles",
            field=models.IntegerField(default=0, null=True),
        ),
    ]