# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 05:42
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('street_address', models.CharField(blank=True, default='', max_length=256)),
                ('city', models.CharField(blank=True, default='', max_length=128)),
                ('state', models.CharField(blank=True, default='', max_length=128)),
                ('postal_code', models.CharField(blank=True, max_length=64, null=True)),
                ('country', models.CharField(blank=True, default='', max_length=128)),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='', max_length=16)),
                ('service_type', models.CharField(blank=True, choices=[('ELECTRICAL', 'Electrical'), ('PLUMBING', 'Plumbing'), ('CARPENTRY', 'Carpentry'), ('LABOR', 'Labor')], default='', max_length=16)),
                ('service_locality', models.CharField(blank=True, default='', max_length=128)),
            ],
        ),
    ]
