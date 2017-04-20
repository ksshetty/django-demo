from rest_framework import serializers

from vendor.models import Vendor


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'