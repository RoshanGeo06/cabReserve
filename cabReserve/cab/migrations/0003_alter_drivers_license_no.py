# Generated by Django 4.1 on 2022-10-31 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cab', '0002_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivers',
            name='license_no',
            field=models.IntegerField(verbose_name='Licence'),
        ),
    ]
