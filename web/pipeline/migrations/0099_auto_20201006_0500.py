# Generated by Django 2.2.13 on 2020-10-06 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0098_auto_20200930_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasource',
            name='sub_resource_id',
            field=models.CharField(help_text='Sub-resource ID for datasets from Open Government', max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='permalink_id',
            field=models.CharField(help_text='Permalink ID for datasets from the BC Data Catalogue', max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='resource_id',
            field=models.CharField(help_text='Resource ID for datasets from the BC Data Catalogue or Open Government', max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='source',
            field=models.CharField(choices=[('internal', 'Provided by Network BC team'), ('databc', 'BC Data Catalogue'), ('statscan', 'Statistics Canada'), ('openca', 'Open Government (Canada)')], max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='source_type',
            field=models.CharField(choices=[('csv', 'CSV'), ('api', 'DATABC API'), ('shp', 'SHP')], max_length=127, null=True),
        ),
    ]
