from rest_framework import serializers

from work_request.models import WorkRequest


class WorkRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkRequest
        fields = '__all__'