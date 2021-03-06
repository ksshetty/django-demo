# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 05:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(blank=True, default='', max_length=256)),
                ('city', models.CharField(blank=True, default='', max_length=128)),
                ('state', models.CharField(blank=True, default='', max_length=128)),
                ('postal_code', models.CharField(blank=True, max_length=64, null=True)),
                ('country', models.CharField(blank=True, default='', max_length=128)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to='vendor.Vendor')),
                ('requestor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='customer.Customer')),
            ],
        ),
    ]
