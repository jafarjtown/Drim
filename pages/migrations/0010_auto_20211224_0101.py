# Generated by Django 3.1.7 on 2021-12-24 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_page_verify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
