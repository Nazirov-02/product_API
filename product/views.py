from django.db.models import Avg
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
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from rest_framework.permissions import AllowAny
from .models import Product,Comment,Image,Category
from .serializers import ProductSerializer, CategorySerializer, CommentSerializer, ImageSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .permissions import CanDeletePermission,CreatePermission
from rest_framework import viewsets

# Product classes

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if self.action == 'list' or self.action == 'create':
            return Product.objects.prefetch_related('images', 'comments','likes')
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return Product.objects.annotate(avg_rating=Avg('comments__rating')).prefetch_related('likes')
        return super().get_queryset()

    @method_decorator(cache_page(60))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductViewSet, self).dispatch(request, *args, **kwargs)

# class ProductListOrCreate(ListCreateAPIView):
#     queryset = Product.objects.prefetch_related('likes')
#     serializer_class = ProductSerializer
#     permission_classes = [CanDeletePermission]
#     def get_queryset(self):
#         queryset = Product.objects.all().prefetch_related('images').prefetch_related('comments')
#         return queryset
#
#
# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.annotate(avg_rating=Avg('comments__rating'))
#     serializer_class = ProductSerializer
#     permission_classes = [CanDeletePermission]


# Category classes

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CreatePermission]

# class CategoryListOrCreate(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [CreatePermission]
#
# class CategoryDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [AllowAny]

#     Comment classes


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CreatePermission, CanDeletePermission]

# class CommentListOrCreate(ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [CreatePermission]
#
# class CommentDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [CanDeletePermission]

#     Image classes


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

# class ImageListOrCreate(ListCreateAPIView):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#     permission_classes = [AllowAny]
#
# class ImageDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#     permission_classes = [AllowAny]



