# Generated by Django 4.0.6 on 2022-07-16 07:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0003_remove_reservation_attendance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('token', models.CharField(max_length=60)),
                ('confirmed', models.BooleanField(default=False, null=True)),
                ('recognition', models.BooleanField(default=False, null=True)),
                ('attendance_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.students')),
            ],
        ),
    ]
