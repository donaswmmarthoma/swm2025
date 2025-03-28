# Generated by Django 5.1.4 on 2025-02-14 05:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swmapp', '0014_public_dustbin_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='WasteUpdates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(max_length=60)),
                ('date', models.DateField(auto_now_add=True)),
                ('dustbin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swmapp.public_dustbin_register')),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swmapp.logintable')),
            ],
        ),
    ]
