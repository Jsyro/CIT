# Generated by Django 2.2.16 on 2022-03-19 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0160_merge_20220319_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkageWithCensus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bc_fire_zone_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pipeline.WildfireZone')),
                ('census_subdivision_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pipeline.CEN_PROF_DETAILED_CSD_ATTRS_SP')),
                ('economic_region_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pipeline.CensusEconomicRegion')),
                ('local_health_area_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pipeline.HealthAuthorityBoundary')),
                ('regional_district_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pipeline.RegionalDistrict')),
                ('school_district_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pipeline.SchoolDistrict')),
                ('tourism_region_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pipeline.TourismRegion')),
                ('tsunami_notification_zone_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pipeline.TsunamiZone')),
            ],
        ),
    ]
