from rest_framework import serializers

from product.models import Product, Comment, Image, Category


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    class Meta:
        model = Comment
        fields = ['id','comment','product','product_name','rating']

class ImageSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    class Meta:
        model = Image
        fields = ['id','image','product','product_name']


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    category_name = serializers.CharField(source='category.title', read_only=True)
    likes = serializers.SerializerMethodField()
    liked = serializers.SerializerMethodField()
    avg_rating = serializers.FloatField(read_only=True)

    def get_likes(self, instance):
        user = self.context['request'].user
        if not user.is_authenticated:
            return False
        return instance.likes.filter(id=user.id).exists()

    def get_liked(self, instance):
        return list(instance.likes.values_list('username', flat=True))


    class Meta:
        model = Product
        fields = ['id','likes','liked','comments','category','category_name','name','description','quantity','discount','price','images','avg_rating']