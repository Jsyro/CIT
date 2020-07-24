# Generated by Django 2.2.13 on 2020-07-23 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0041_auto_20200722_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='cbc_phase',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='community',
            name='last_mile_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='community',
            name='transport_mile_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='hexuid',
            field=models.ForeignKey(db_column='hexuid', help_text='ID of spatial hex used to color province by connectivity quality.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='community', to='pipeline.Hex'),
        ),
        migrations.AlterField(
            model_name='locationdistance',
            name='distance',
            field=models.DecimalField(blank=True, decimal_places=4, help_text='Driving distance from community to Location (km)', max_digits=24, null=True),
        ),
    ]
