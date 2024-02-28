# Generated by Django 4.1 on 2022-11-12 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cab', '0011_remove_drivers_vehicle_delete_destination_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNo', models.IntegerField()),
                ('boarding', models.CharField(max_length=120)),
                ('destination', models.CharField(max_length=120)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]