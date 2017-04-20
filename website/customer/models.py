from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models


class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        default='',
        blank=True,
        null=True,
    )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    mobile_number = models.CharField(
        validators=[phone_regex],
        max_length=16,
        blank=True
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
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

    GENDER = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )

    gender = models.CharField(
        max_length=16,
        choices=GENDER,
        blank=True,
        default='',
    )

    def __str__(self):
        return "Customer/%s %s" % (self.name, self.mobile_number)
