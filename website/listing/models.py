from __future__ import unicode_literals

from django.db import models

from customer.models import Customer


class Listing(models.Model):
    class Meta:
        abstract = True

    PROPERTY_TYPE = (
        ('RESIDENTIAL', 'Residential'),
        ('COMMERCIAL', 'Commercial'),
        ('AGRICULTURAL', 'Agricultural'),
        ('PG/HOSTEL', 'PG/Hostel')
    )

    property_type = models.CharField(
        max_length=30,
        choices=PROPERTY_TYPE,
        blank=True,
        default='',
    )

    listing_owner = models.ForeignKey(
        Customer,
        blank=True,
        null=True,
        related_name='%(app_label)s_%(class)s_listing_owner',
    )

    street_address = models.CharField(
        max_length=256,
        blank=True,
        default='',
    )

    city = models.CharField(
        max_length=128,
        blank=True,
        default='',
    )

    state = models.CharField(
        max_length=128,
        blank=True,
        default='',
    )

    postal_code = models.CharField(
        blank=True,
        null=True,
        max_length=64,
    )

    country = models.CharField(
        max_length=128,
        blank=True,
        default='',
    )


class ResidentialListing(Listing):
    class Meta(Listing.Meta):
        pass

    num_bedrooms = models.PositiveIntegerField(

    )

    num_bathrooms = models.PositiveIntegerField(

    )

    num_balconies = models.PositiveIntegerField(

    )
