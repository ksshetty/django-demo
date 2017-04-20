from rest_framework import viewsets

from customer.models import Customer

from customer.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    logging_methods = ['POST', 'PUT', 'PATCH', 'DELETE']
