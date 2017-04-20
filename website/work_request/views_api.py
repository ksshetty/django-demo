from rest_framework import viewsets

from work_request.models import WorkRequest
from work_request.serializers import WorkRequestSerializer


class WorkRequesViewSet(viewsets.ModelViewSet):
    queryset = WorkRequest.objects.all()
    serializer_class = WorkRequestSerializer
    logging_methods = ['POST', 'PUT', 'PATCH', 'DELETE']