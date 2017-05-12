from rest_framework import viewsets

from listing.models import ResidentialListing
from listing.serializers import ResidentialSerializer


class ResidentialListingViewSet(viewsets.ModelViewSet):
    queryset = ResidentialListing.objects.all()
    serializer_class = ResidentialSerializer
    logging_methods = ['POST', 'PUT', 'PATCH', 'DELETE']