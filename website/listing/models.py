from __future__ import unicode_literals

from django.db import models

from customer.models import Customer


class Listing(models.Model):

    PROPERTY_TYPE = (
        ('RESIDENTIAL', 'Residential'),
        ('COMMERCIAL', 'Commercial'),
        ('AGRICULTURAL', 'Agricultural'),
        ('PG/HOSTEL', 'PG/Hostel')
    )

    WATER_SOURCE = (
        ('CORPORATION', 'Corporation'),
        ('BOREWELL', 'Borewell'),
        ('TANKERS', 'Tankers')
    )

    SECURITY_AVAILABILITY_HOURS = (
        ('8 HOURS', '8 hours'),
        ('16 HOURS', '16 hours'),
        ('24 HOURS', '24 hours')
    )

    PG_AVAILABILITY = (
        ('MALE_ONLY', 'Male Only'),
        ('FEMALE_ONLY', 'Female Only'),
        ('CO-ED', 'Co-ed')
    )

    OCCUPANCY_AVAILABILITY = (
        ('SINGLE_ONLY', 'Single Only'),
        ('SHARING_ONLY', 'Sharing Only'),
        ('BOTH', 'Both')
    )

    CONSTRUCTION_AGE = (
        ('LESS THAN A YEAR OLD', 'Less than a year old'),
        ('1 TO 3 YEARS OLD', '1 to 3 years old'),
        ('3 TO 5 YEARS OLD', '3 to 5 years old'),
        ('5 TO 10 YEARS OLD', '5 to 10 years old'),
        ('GREATER THAN 10 YEARS OLD', 'Greater than 10 years old'),
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

    # Residential Listing Attributes
    num_bedrooms = models.PositiveIntegerField(

    )

    num_bathrooms = models.PositiveIntegerField(

    )

    num_balconies = models.PositiveIntegerField(

    )

    # Office Space attributes
    num_washrooms = models.PositiveIntegerField(
        default=0,
    )

    furnished = models.BooleanField(
        default=False,
    )

    num_floors = models.PositiveIntegerField(
        default=1,
    )

    seating_capacity = models.PositiveIntegerField(
        default=0,
    )

    num_parking_spaces = models.PositiveIntegerField(
        default=0,
    )

    area = models.IntegerField(
        default=0,
    )

    date_available = models.DateTimeField(
        blank=True,
        null=True,
    )

    age_of_construction = models.CharField(
        max_length=30,
        choices=CONSTRUCTION_AGE,
        default=''
    )

    expected_monthly_rent = models.FloatField(
        blank=True,
        null=True,
    )

    other_charges = models.CharField(
        max_length=512,
        blank=True,
        null=True,
    )

    security_deposit_amount = models.FloatField(
        blank=True,
        null=True,
    )

    maintenance_charges = models.FloatField(
        blank=True,
        null=True,
    )

    # Commercial Shop or Showroom related fields

    pantry = models.BooleanField(
        default=False,
    )

    corner_shop = models.BooleanField(
        default=False,
    )

    main_road_facing = models.BooleanField(
        default=False,
    )

    # Agricultural property / farmhouse related attributes
    swimming_pool = models.BooleanField(
        default=False,
    )

    garden_availability = models.BooleanField(
        default=False,
    )

    garden_area = models.IntegerField(
        default=0
    )

    club_house = models.BooleanField(
        default=False,
    )

    play_area_availability = models.BooleanField(
        default=False,
    )

    play_area = models.IntegerField(
        default=0
    )

    day_care_availability = models.BooleanField(
        default=False,
    )

    power_backup_availability = models.BooleanField(
        default=False,
    )

    water_source = models.CharField(
        max_length=30,
        choices=WATER_SOURCE,
        blank=True,
        default='',
    )

    security_hours = models.CharField(
        max_length=30,
        choices=SECURITY_AVAILABILITY_HOURS,
        blank=True,
        default='',
    )

    # PG or Hostel related fields
    pg_availability = models.CharField(
        max_length=30,
        choices=PG_AVAILABILITY,
        blank=True,
        default='',
    )

    pg_occupancy_availability = models.CharField(
        max_length=30,
        choices=OCCUPANCY_AVAILABILITY,
        blank=True,
        default='',
    )

    food_availability = models.BooleanField(
        default=False,
    )

    attached_bathroom = models.BooleanField(
        default=False,
    )

    attached_balcony = models.BooleanField(
        default=False,
    )

