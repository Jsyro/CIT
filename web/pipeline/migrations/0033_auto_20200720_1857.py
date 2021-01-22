# Generated by Django 2.2.13 on 2020-07-20 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0032_municipality'),
    ]

    operations = [
        migrations.AddField(
            model_name='civicfacility',
            name='bus_cat_cl',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='civicfacility',
            name='bus_cat_ds',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='civicfacility',
            name='keywords',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clinic',
            name='hours',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clinic',
            name='sv_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='diagnosticfacility',
            name='ser_cd_dsc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='economicproject',
            name='eao_project_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='economicproject',
            name='flnro_project_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='economicproject',
            name='project_category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='economicproject',
            name='project_comments',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='economicproject',
            name='project_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='economicproject',
            name='proponent',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='firstresponder',
            name='keywords',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='architect',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='clean_energy_ind',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='construction_jobs',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='construction_subtype',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='construction_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='developer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='estimated_cost',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='federal_funding',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='green_building_desc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='green_building_ind',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='municipal_funding',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='operating_jobs',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='project_category_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='project_comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='project_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='project_stage',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='project_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='project_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='provinvial_funding',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='standardized_completion_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='standardized_start_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='naturalresourceproject',
            name='update_activity',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='district_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='public_or_independent',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='school_education_level',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='timberfacility',
            name='bus_cat_ds',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
