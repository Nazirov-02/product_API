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


from rest_framework.permissions import AllowAny
from .models import Product,Comment,Image,Category
from .serializers import ProductSerializer, CategorySerializer, CommentSerializer, ImageSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .permissions import CanDeletePermission,CreatePermission

# Product classes

class ProductListOrCreate(ListCreateAPIView):
    queryset = Product.objects.prefetch_related('likes')
    serializer_class = ProductSerializer
    permission_classes = [CanDeletePermission]
    def get_queryset(self):
        queryset = Product.objects.all().prefetch_related('images').prefetch_related('comments')
        return queryset


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.annotate(avg_rating=Avg('comments__rating'))
    serializer_class = ProductSerializer
    permission_classes = [CanDeletePermission]


# Category classes

class CategoryListOrCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CreatePermission]

class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

#     Comment classes

class CommentListOrCreate(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CreatePermission]

class CommentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CanDeletePermission]

#     Image classes

class ImageListOrCreate(ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [AllowAny]

class ImageDetail(RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [AllowAny]



