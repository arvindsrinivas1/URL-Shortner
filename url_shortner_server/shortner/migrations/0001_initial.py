# Generated by Django 3.2.1 on 2022-10-03 15:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Link",
            fields=[
                ("long_url", models.CharField(max_length=2083)),
                (
                    "special_code",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("stub", models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
