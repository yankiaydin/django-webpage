# Generated by Django 3.2.4 on 2021-06-14 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('web_page', models.URLField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('job', models.CharField(choices=[('', ''), ('Architect', 'Architect'), ('Freelance Designer', 'Freelance Designer'), ('Constructor', 'Constructor'), ('Other', 'Other')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]