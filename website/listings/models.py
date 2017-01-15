from django.contrib.auth.models import User
from django.db import models


class Listing(models.Model):
    user = models.ForeignKey(User, default=1)
    property_type = models.CharField(max_length=100)
    property_size = models.IntegerField()
    year_built = models.DateField()
    address = models.CharField(max_length=500)
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()

    def __str__(self):
        return u'PropertyType: %s, Size: %s, Bedrooms: %s, Bathrooms: %s, Address: %s' % \
               (self.property_type, self.property_size, self.num_bedrooms, self.num_bathrooms, self.address)