# Generated by Django 5.1.7 on 2025-04-03 00:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_semester_sections'),
        ('classes', '0004_lecture_plan_course_lecture_plan_module_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture_plan',
            name='semester',
            field=models.ForeignKey(default='BCA(H)-2023-1', on_delete=django.db.models.deletion.CASCADE, to='academics.semester'),
            preserve_default=False,
        ),
    ]
