from rest_framework import viewsets

from listing.models import Listing
from listing.serializers import ListingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    logging_methods = ['POST', 'PUT', 'PATCH', 'DELETE']