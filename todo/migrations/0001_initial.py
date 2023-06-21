# Generated by Django 4.2.2 on 2023-06-16 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ToDo",
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
                ("user_name", models.CharField(max_length=20)),
                ("task", models.CharField(max_length=200)),
                (
                    "description",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                ("status", models.CharField(default="Pending", max_length=20)),
                (
                    "file",
                    models.FileField(
                        default=None, max_length=150, null=True, upload_to="files/"
                    ),
                ),
            ],
        ),
    ]