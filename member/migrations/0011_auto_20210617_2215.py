# Generated by Django 3.2.4 on 2021-06-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0010_auto_20210617_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='job',
            new_name='role',
        ),
        migrations.AlterField(
            model_name='architect',
            name='experience',
            field=models.IntegerField(blank=True),
        ),
    ]
