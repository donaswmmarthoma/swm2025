# Generated by Django 5.1.4 on 2025-03-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swmapp', '0026_dustbinreg_collection_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='public_dustbin_register',
            name='location',
        ),
        migrations.AddField(
            model_name='public_dustbin_register',
            name='latitude',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='public_dustbin_register',
            name='longitude',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
