# Generated by Django 5.0.6 on 2024-06-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todolistapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="completed",
            field=models.BooleanField(default=False),
        ),
    ]