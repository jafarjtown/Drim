# Generated by Django 3.1.7 on 2021-12-24 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20211224_0101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='forbiddenword',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='group',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='updated_at',
        ),
    ]
