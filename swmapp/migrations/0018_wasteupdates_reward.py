# Generated by Django 5.1.4 on 2025-02-14 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swmapp', '0017_alter_wasteupdates_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='wasteupdates',
            name='reward',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
