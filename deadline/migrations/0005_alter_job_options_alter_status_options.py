# Generated by Django 4.0.10 on 2024-07-20 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deadline', '0004_rename_task_project_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': 'Ish turi', 'verbose_name_plural': 'Ish turlari'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Jarayon', 'verbose_name_plural': 'Jarayonlar'},
        ),
    ]