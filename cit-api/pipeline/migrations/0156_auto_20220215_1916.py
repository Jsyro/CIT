# Generated by Django 2.2.16 on 2022-02-15 19:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0155_auto_20210426_1953'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BCFloodplain',
        ),
        migrations.RemoveField(
            model_name='civicleader',
            name='community',
        ),
        migrations.RemoveField(
            model_name='closedmill',
            name='location_ptr',
        ),
        migrations.RemoveField(
            model_name='eaoprojects',
            name='location_ptr',
        ),
        migrations.DeleteModel(
            name='PermittedMajorMines',
        ),
        migrations.AlterField(
            model_name='user',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='CivicLeader',
        ),
        migrations.DeleteModel(
            name='ClosedMill',
        ),
        migrations.DeleteModel(
            name='EAOProjects',
        ),
    ]
