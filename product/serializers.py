from rest_framework import serializers

from product.models import Product, Comment, Image, Category


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name', read_only=True)
    class Meta:
        model = Comment
        fields = ['id','comment','product']

class ImageSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name', read_only=True)
    class Meta:
        model = Image
        fields = ['id','image','product']


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True,read_only=True)
    comments = CommentSerializer(many=True,read_only=True)
    category = serializers.CharField(source='category.title',read_only=True)

    class Meta:
        model = Product
        fields = '__all__'