# Generated by Django 5.1.7 on 2025-04-06 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='lecture',
            options={'verbose_name_plural': 'Lectures'},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'verbose_name_plural': 'Modules'},
        ),
    ]
