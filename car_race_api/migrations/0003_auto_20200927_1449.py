# Generated by Django 3.1.1 on 2020-09-27 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_race_api', '0002_auto_20200927_1443'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AuthenticatedPlayer',
            new_name='AuthPlayer',
        ),
    ]
