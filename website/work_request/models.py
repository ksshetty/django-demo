from __future__ import unicode_literals

from django.db import models

from customer.models import Customer
from vendor.models import Vendor


class WorkRequest(models.Model):
    requestor = models.ForeignKey(
        Customer,
        blank = True,
        null = True,
        related_name = 'customer',
    )

    assigned_to = models.ForeignKey(
        Vendor,
        blank = True,
        null = True,
        related_name = 'vendor'
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

    STATE = (
        ('REQUESTED', 'Requested'),
        ('VENDOR_NOTIFIED', 'VendorNotified'),
        ('VENDOR_ACCEPTED', 'VendorAccepted'),
        ('IN_PROGRESS', 'InProgress'),
        ('VENDOR_COMPLETE', 'VendorComplete'),
        ('CUSTOMER_COMPLETE', 'CustomerComplete'),
    )

    state = models.CharField(
        max_length=16,
        choices=STATE,
        blank=True,
        default='',
    )

    SERVICE_TYPE = (
        ('ELECTRICAL', 'Electrical'),
        ('PLUMBING', 'Plumbing'),
        ('CARPENTRY', 'Carpentry'),
        ('LABOR', 'Labor'),
    )

    service_type = models.CharField(
        max_length=16,
        choices=SERVICE_TYPE,
        blank=True,
        default='',
    )

    def __str__(self):
        return "Work Request/%s %s" % (self.name, self.mobile_number)
