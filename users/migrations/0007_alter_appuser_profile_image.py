# Generated by Django 5.0.6 on 2024-07-06 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_appuser_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appuser",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="media/profile/"),
        ),
    ]
