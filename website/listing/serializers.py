from rest_framework import serializers

from listing.models import ResidentialListing


class ResidentialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResidentialListing
        fields = '__all__'