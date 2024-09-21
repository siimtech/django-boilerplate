# Generated by Django 5.0.6 on 2024-07-04 08:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_admin_options_alter_appuser_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="SocialAccount",
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
                ("kakao_id", models.CharField(blank=True, max_length=255, null=True)),
                ("naver_id", models.CharField(blank=True, max_length=255, null=True)),
                ("google_id", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="users.appuser"),
                ),
            ],
        ),
    ]
