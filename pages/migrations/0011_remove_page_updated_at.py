# Generated by Django 3.1.7 on 2021-12-24 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20211224_0101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='updated_at',
        ),
    ]
