# Generated by Django 5.0.1 on 2024-01-20 11:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=24)),
                ("content", models.TextField()),
                ("like", models.IntegerField()),
            ],
        ),
    ]
