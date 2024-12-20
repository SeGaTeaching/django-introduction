# Generated by Django 5.1.3 on 2024-11-15 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_intro', '0005_student_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enroll_date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_intro.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_intro.student')),
            ],
        ),
    ]
