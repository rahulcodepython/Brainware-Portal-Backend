# Generated by Django 5.1.7 on 2025-04-01 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class_routine',
            name='semester',
            field=models.ForeignKey(default='BCA(H)-2024-1', on_delete=django.db.models.deletion.CASCADE, to='academics.semester'),
            preserve_default=False,
        ),
    ]
