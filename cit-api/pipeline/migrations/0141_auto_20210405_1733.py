# Generated by Django 2.2.16 on 2021-04-05 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0140_merge_20210401_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='nearest_research_center',
            field=models.ForeignKey(blank=True, db_column='nearest_research_centre', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='research_centre', to='pipeline.ResearchCentreDistance'),
        ),
        migrations.RenameField(
            model_name='opportunity',
            old_name='nearest_research_center',
            new_name='nearest_research_centre',
        ),
    ]
