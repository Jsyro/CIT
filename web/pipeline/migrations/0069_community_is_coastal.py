# Generated by Django 2.2.13 on 2020-08-29 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0068_auto_20200829_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='is_coastal',
            field=models.NullBooleanField(),
        ),
    ]
