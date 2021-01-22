# Generated by Django 2.2.13 on 2020-10-23 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0103_censussubdivision_employment_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasource',
            name='source',
            field=models.CharField(choices=[('internal', 'Provided by Network BC team'), ('databc', 'BC Data Catalogue'), ('statscan', 'Statistics Canada'), ('openca', 'Open Government (Canada)'), ('other', 'Other')], max_length=127, null=True),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('location_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pipeline.Location')),
                ('project_id', models.IntegerField(blank=True, null=True)),
                ('project_description', models.TextField(blank=True, null=True)),
                ('estimated_cost', models.IntegerField(blank=True, null=True)),
                ('update_activity', models.TextField(blank=True, null=True)),
                ('environmental_assessment_stage', models.CharField(blank=True, max_length=255, null=True)),
                ('construction_type', models.CharField(blank=True, max_length=255, null=True)),
                ('construction_subtype', models.CharField(blank=True, max_length=255, null=True)),
                ('project_type', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('municipality', models.CharField(blank=True, max_length=255, null=True)),
                ('developer', models.CharField(blank=True, max_length=255, null=True)),
                ('architect', models.CharField(blank=True, max_length=255, null=True)),
                ('project_status', models.CharField(blank=True, max_length=255, null=True)),
                ('project_stage', models.CharField(blank=True, max_length=255, null=True)),
                ('project_category_name', models.CharField(blank=True, max_length=255, null=True)),
                ('public_funding_ind', models.IntegerField(blank=True, null=True)),
                ('provinvial_funding', models.IntegerField(blank=True, null=True)),
                ('federal_funding', models.IntegerField(blank=True, null=True)),
                ('municipal_funding', models.IntegerField(blank=True, null=True)),
                ('other_public_funding', models.IntegerField(blank=True, null=True)),
                ('green_building_ind', models.IntegerField(blank=True, null=True)),
                ('green_building_desc', models.CharField(blank=True, max_length=255, null=True)),
                ('clean_energy_ind', models.IntegerField(blank=True, null=True)),
                ('indigenous_ind', models.IntegerField(blank=True, null=True)),
                ('indigenous_names', models.CharField(blank=True, max_length=255, null=True)),
                ('indigenous_agreement', models.TextField(blank=True, null=True)),
                ('construction_jobs', models.IntegerField(blank=True, null=True)),
                ('operating_jobs', models.IntegerField(blank=True, null=True)),
                ('start_date', models.CharField(blank=True, max_length=255, null=True)),
                ('completion_date', models.CharField(blank=True, max_length=255, null=True)),
                ('standardized_start_date', models.CharField(blank=True, max_length=255, null=True)),
                ('standardized_completion_date', models.CharField(blank=True, max_length=255, null=True)),
                ('first_entry_date', models.CharField(blank=True, max_length=255, null=True)),
                ('last_update', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_fields', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('id',),
                'unique_together': {('project_id', 'last_update')},
            },
            bases=('pipeline.location',),
        ),
    ]
