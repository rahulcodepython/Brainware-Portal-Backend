# Generated by Django 5.1.7 on 2025-03-31 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='semester_course',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
