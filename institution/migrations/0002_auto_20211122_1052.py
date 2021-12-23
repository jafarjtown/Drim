# Generated by Django 3.1.7 on 2021-11-22 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institution', '0001_initial'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='pages',
            field=models.ManyToManyField(blank=True, to='pages.Page'),
        ),
        migrations.AddField(
            model_name='institution',
            name='programmes',
            field=models.ManyToManyField(blank=True, related_name='institution', to='institution.Programme'),
        ),
    ]