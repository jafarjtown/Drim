# Generated by Django 3.1.7 on 2021-11-25 22:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0002_page_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='admins',
            field=models.ManyToManyField(related_name='pages', to=settings.AUTH_USER_MODEL),
        ),
    ]
