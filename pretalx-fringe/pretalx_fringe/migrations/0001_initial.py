# Generated by Django 4.2.5 on 2024-10-18 20:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("event", "0035_created_updated_everywhere"),
    ]

    operations = [
        migrations.CreateModel(
            name="FringeActivity",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("url", models.URLField()),
                ("location", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("why", models.TextField()),
                ("starts", models.DateTimeField()),
                ("ends", models.DateTimeField()),
                ("cost", models.CharField(max_length=255, null=True)),
                ("registration", models.CharField(max_length=255, null=True)),
                ("contact", models.EmailField(max_length=254)),
                ("online", models.BooleanField(default=False)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fringe_activities",
                        to="event.event",
                    ),
                ),
                (
                    "submitter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
