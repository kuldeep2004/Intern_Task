from rest_framework import serializers
from .models import Product, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'discountPercentage', 'rating', 'stock', 'brand', 'category', 'thumbnail', 'images']


