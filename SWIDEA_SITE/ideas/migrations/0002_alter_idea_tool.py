# Generated by Django 5.0.1 on 2024-01-17 00:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ideas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="idea",
            name="tool",
            field=models.CharField(
                choices=[("Django", "Django"), ("Django", "Django")],
                max_length=24,
                verbose_name="예상 개발툴",
            ),
        ),
    ]
