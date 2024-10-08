# Generated by Django 4.0.10 on 2024-07-20 05:53

import deadline.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('image', models.ImageField(null=True, upload_to=deadline.models.upload_to)),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('direction', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(max_length=500, null=True)),
                ('job', models.ManyToManyField(to='deadline.job')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deadline.task')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Proyekt',
                'verbose_name_plural': 'Proyektlar',
            },
        ),
    ]
