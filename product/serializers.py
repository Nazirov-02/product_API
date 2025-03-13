from rest_framework import serializers

from product.models import Product, Comment, Image, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','comment']

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Image
        fields = ['id','image','image_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True,read_only=True)
    comments = CommentSerializer(many=True,read_only=True)
    category = serializers.CharField(source='category.title',read_only=True)

    class Meta:
        model = Product
        fields = '__all__'