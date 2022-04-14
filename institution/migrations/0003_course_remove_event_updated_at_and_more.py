# Generated by Django 4.0.2 on 2022-04-13 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activities', '0004_activity_updated'),
        ('posts', '0007_remove_post_group_post_related_to_story'),
        ('groups', '0006_group_posts'),
        ('accounts', '0003_contact_student_alter_user_options_and_more'),
        ('institution', '0002_auto_20211122_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('updated', models.DateTimeField(auto_created=True, auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('slogan', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='event',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='institution',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='programme',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='event',
            name='updated',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='activities',
            field=models.ManyToManyField(to='activities.Activity'),
        ),
        migrations.AddField(
            model_name='institution',
            name='address',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institution',
            name='administrator',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='administrator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='institution',
            name='blogs',
            field=models.ManyToManyField(related_name='institution', to='posts.Post'),
        ),
        migrations.AddField(
            model_name='institution',
            name='cover_img',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institution',
            name='groups',
            field=models.ManyToManyField(related_name='institution', to='groups.Group'),
        ),
        migrations.AddField(
            model_name='institution',
            name='logo',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institution',
            name='slogan',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institution',
            name='subscribers',
            field=models.ManyToManyField(related_name='institutions_subscribes', to='accounts.Student'),
        ),
        migrations.AddField(
            model_name='institution',
            name='tutors',
            field=models.ManyToManyField(blank=True, to='accounts.Teacher'),
        ),
        migrations.AddField(
            model_name='institution',
            name='updated',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='institution',
            name='website_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programme',
            name='updated',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='courses',
            field=models.ManyToManyField(blank=True, to='institution.Course'),
        ),
    ]