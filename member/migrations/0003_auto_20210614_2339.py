# Generated by Django 3.2.4 on 2021-06-14 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("member", "0002_auto_20210614_2159"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="job",
        ),
        migrations.AlterField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
