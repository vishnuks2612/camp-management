# Generated by Django 5.0.2 on 2024-02-20 04:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='camp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.campmodel'),
        ),
    ]
