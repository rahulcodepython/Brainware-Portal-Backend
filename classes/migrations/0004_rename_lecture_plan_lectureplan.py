# Generated by Django 5.1.7 on 2025-04-08 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0004_semester_course_faculty'),
        ('authentication', '0003_alter_faculty_profile_options_and_more'),
        ('classes', '0003_alter_attendance_options_alter_class_routine_options_and_more'),
        ('courses', '0002_alter_course_options_alter_lecture_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lecture_Plan',
            new_name='LecturePlan',
        ),
    ]
