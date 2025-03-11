from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from product.serializers import ProductSerializer


# Create your views here.
class ProductList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, pk, format=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)