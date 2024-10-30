from rest_framework import serializers

from products.models import Category, Product, ProductImage, ProductColor


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['is_deleted', 'is_active']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ['product']

class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        exclude = ['product']
        # fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product_colors = ProductColorSerializer(many=True, read_only=True)
    product_images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = [ 'product_colors', 'product_images']

        # exclude = ['is_deleted', 'is_active',]

class ProductDetailSerializer(serializers.ModelSerializer):
    product_colors = ProductColorSerializer(many=True, read_only=True)
    product_images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['__all__', 'product_colors', 'product_images']
        # exclude = ['is_deleted', 'is_active',]