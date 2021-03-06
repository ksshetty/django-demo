# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-21 02:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResidentialListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(blank=True, choices=[('RESIDENTIAL', 'Residential'), ('COMMERCIAL', 'Commercial'), ('AGRICULTURAL', 'Agricultural'), ('PG/HOSTEL', 'PG/Hostel')], default='', max_length=30)),
                ('street_address', models.CharField(blank=True, default='', max_length=256)),
                ('city', models.CharField(blank=True, default='', max_length=128)),
                ('state', models.CharField(blank=True, default='', max_length=128)),
                ('postal_code', models.CharField(blank=True, max_length=64, null=True)),
                ('country', models.CharField(blank=True, default='', max_length=128)),
                ('num_bedrooms', models.PositiveIntegerField()),
                ('num_bathrooms', models.PositiveIntegerField()),
                ('num_balconies', models.PositiveIntegerField()),
                ('listing_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_residentiallisting_listing_owner', to='customer.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
