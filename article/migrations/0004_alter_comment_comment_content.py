# Generated by Django 3.2.4 on 2021-06-24 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20210621_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=models.CharField(blank=True, max_length=100, verbose_name='Content'),
        ),
    ]