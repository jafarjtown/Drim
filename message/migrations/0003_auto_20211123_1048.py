# Generated by Django 3.1.7 on 2021-11-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20211123_0625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]