# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workrequest',
            name='service_type',
            field=models.CharField(blank=True, choices=[('ELECTRICAL', 'Electrical'), ('PLUMBING', 'Plumbing'), ('CARPENTRY', 'Carpentry'), ('LABOR', 'Labor')], default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='state',
            field=models.CharField(blank=True, choices=[('REQUESTED', 'Requested'), ('VENDOR_NOTIFIED', 'VendorNotified'), ('VENDOR_ACCEPTED', 'VendorAccepted'), ('IN_PROGRESS', 'InProgress'), ('VENDOR_COMPLETE', 'VendorComplete'), ('CUSTOMER_COMPLETE', 'CustomerComplete')], default='', max_length=16),
        ),
    ]
