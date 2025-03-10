# Generated by Django 2.2.28 on 2023-04-26 21:14

from django.db import migrations

def remove_status_new(apps, schema_editor):
    opportunity = apps.get_model("pipeline", "Opportunity")
    approval_status = apps.get_model("pipeline", "ApprovalStatus")

    # Update NEW & NWED statuses to be PEND
    new_opportunities = opportunity.objects.filter(approval_status_id__in=['NEW','NWED']).update(approval_status_id='PEND')

    # remove NEW & NWED from pipeline_approvalstatus
    old_approval_statuses = approval_status.objects.filter(status_code__in=['NEW','NWED']).delete()

def add_status_new(apps, schema_editor):
    approval_status = apps.get_model("pipeline", "ApprovalStatus")

    approval_status.objects.update_or_create(status_name='New', status_description='Opportunity has just been submitted',status_code='NEW')
    approval_status.objects.update_or_create(status_name='New - Edited', status_description='Opportunity has been udpate by EDO for further review',status_code='NWED')


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0183_remove_softdelete_records_opportunity_view'),
    ]

    operations = [
        migrations.RunPython(remove_status_new, add_status_new),
        migrations.AlterModelOptions(
            name='opportunity',
            options={'ordering': ('id',)},
        ),
    ]
