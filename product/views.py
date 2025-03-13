

#
# # Create your views here.
# class ProductList(APIView):
#     permission_classes = (permissions.AllowAny,)
#     def get(self, request, format=None):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
# class ProductDetail(APIView):
#     permission_classes = (permissions.AllowAny,)
#     def get(self, request, pk, format=None):
#         product = Product.objects.get(id=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status, permissions
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class PostListOrCreate(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context



class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context