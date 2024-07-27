from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ecommapp.models import Product
from ecommapp.serializers.product_serializer import ProductSerializer


class ListCreateProductAPIView(APIView):
    def get(self, request) -> Response:
        products = Product.objects.all()
        decoded_data = ProductSerializer(products, many=True)
        return Response(decoded_data.data, status=200)

    def post(self, request) -> Response:
        data = request.data
        decoded_data = ProductSerializer(data=data)
        if not decoded_data.is_valid():
            return Response(decoded_data.errors, status=400)
        decoded_data.save()
        return Response(decoded_data.data, status=201)
