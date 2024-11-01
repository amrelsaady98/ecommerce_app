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
        fields = [
            'product_id', 'code', 'cost_price', 'description', 'image1',
            'name', 'our_price', 'sale_price', 'has_discount', 'total_rating',
            'stock_qty', 'year', 'category',
            'product_colors', 'product_images'
        ]
        # exclude = ['is_deleted', 'is_active',]

class ProductDetailSerializer(serializers.ModelSerializer):
    product_colors = ProductColorSerializer(many=True, read_only=True)
    product_images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['product_id', 'code', 'cost_price', 'description', 'image1',
            'name', 'our_price', 'sale_price', 'has_discount', 'total_rating',
            'stock_qty', 'year', 'category',
            'product_colors', 'product_images']
        # exclude = ['is_deleted', 'is_active',]