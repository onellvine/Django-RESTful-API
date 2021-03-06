# Generated by Django 3.1.5 on 2021-01-30 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SysUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('phone', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'SysUsers',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('cast', models.JSONField()),
                ('category', models.CharField(choices=[('MOV', 'movie'), ('SER', 'series')], default='MOV', max_length=3)),
                ('comments', models.IntegerField(default=0)),
                ('cover_photo', models.ImageField(upload_to='uploads/')),
                ('genre', models.JSONField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('released', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('movie_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='movie_api.movie', verbose_name='Movie')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='SysUser')),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
