# Generated by Django 5.0.2 on 2024-02-20 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp_app', '0008_leaverequestmodel_employeeid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaverequestmodel',
            name='approvalstatus',
        ),
    ]