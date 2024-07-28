from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ecommapp.models import Product
from ecommapp.serializers.product_serializer import ProductSerializer


class ListCreateProductAPIView(APIView):
    def get(self, request) -> Response:
        # can use many filter options : .filter(firstname='Emil').values() or filter(lastname='Refsnes', id=2).values()
        # OR options Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
        # .filter(firstname__startswith='L'); more : www.w3schools.com/django/django_queryset_filter.php
        # products = Product.objects.all().filter(price__gte=50.00)
        products = Product.objects.raw('SELECT * FROM ecommapp_product')
        decoded_data = ProductSerializer(products, many=True)
        return Response(decoded_data.data, status=200)

    def post(self, request) -> Response:
        data = request.data
        decoded_data = ProductSerializer(data=data)
        if not decoded_data.is_valid():
            return Response(decoded_data.errors, status=400)
        decoded_data.save()
        return Response(decoded_data.data, status=201)
