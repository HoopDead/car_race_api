# Generated by Django 3.1.1 on 2020-09-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_race_api', '0006_auto_20200927_1629'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthPlayer',
        ),
        migrations.RemoveField(
            model_name='player',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='player',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='player',
            name='token',
            field=models.CharField(default='', editable=False, max_length=96, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='uid',
            field=models.IntegerField(default=1, editable=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='x_position',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='y_position',
            field=models.IntegerField(null=True),
        ),
    ]
