# Generated by Django 4.1 on 2022-11-07 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cab', '0008_cabuser_alter_drivers_attendees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='vehicle',
        ),
        migrations.RemoveField(
            model_name='drivers',
            name='attendees',
        ),
        migrations.DeleteModel(
            name='Cabuser',
        ),
    ]
