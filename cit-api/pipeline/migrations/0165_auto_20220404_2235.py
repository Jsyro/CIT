# Generated by Django 2.2.16 on 2022-04-04 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0164_auto_20220331_0455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nbdphhspeeds',
            old_name='combined_5_1_gov_supp',
            new_name='combined_50_10_gov_supp',
        ),
        migrations.AddField(
            model_name='phdemographicdistribution',
            name='census_subdivision',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pipeline.CEN_PROF_DETAILED_CSD_ATTRS_SP'),
        ),
        
    ]
