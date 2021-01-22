# Generated by Django 2.2.16 on 2020-11-06 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0112_auto_20201027_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='community',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='community_images/'),
        ),
    ]
