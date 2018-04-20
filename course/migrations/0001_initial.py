# Generated by Django 2.0.1 on 2018-04-12 15:01

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', django.contrib.postgres.fields.jsonb.JSONField(default=list)),
                ('total_student', models.IntegerField(blank=True, default=0)),
                ('total_task', models.IntegerField(blank=True, default=0)),
                ('title', models.CharField(max_length=64)),
                ('introduction', utils.models.RichTextField()),
                ('picture', models.CharField(default='/public/avatar/default.png', max_length=256)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
                ('visible', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'course',
                'ordering': ('create_time',),
            },
        ),
        migrations.CreateModel(
            name='Course_task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField()),
                ('title', models.CharField(max_length=64)),
                ('introduction', utils.models.RichTextField()),
                ('type', models.CharField(max_length=32)),
                ('visible', models.BooleanField(default=True)),
                ('problem', django.contrib.postgres.fields.jsonb.JSONField(default=list)),
                ('small_problem', django.contrib.postgres.fields.jsonb.JSONField(default=list)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'course_task',
                'ordering': ('create_time',),
            },
        ),
        migrations.CreateModel(
            name='CourseAnnouncement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', utils.models.RichTextField()),
                ('visible', models.BooleanField(default=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'course_announcement',
                'ordering': ('-create_time',),
            },
        ),
    ]
