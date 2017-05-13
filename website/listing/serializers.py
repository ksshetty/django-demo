from rest_framework import serializers

from listing.models import Listing


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'