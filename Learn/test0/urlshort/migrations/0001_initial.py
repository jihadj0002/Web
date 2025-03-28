# Generated by Django 5.1.6 on 2025-03-02 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UrlData",
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
                ("url", models.URLField()),
                ("slug", models.SlugField(max_length=15, unique=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
