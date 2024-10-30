from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from core.utils import api_response
from products.models import Category, Product, ProductColor, ProductImage
from products.serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer, ProductImageSerializer, \
    ProductColorSerializer


# Create your views here.


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_all_categories(request):
    try:
        categories = Category.objects.filter(is_active=True, is_deleted=False).all()
        return api_response(
            success=True,
            status_code=status.HTTP_200_OK,
            data=CategorySerializer(categories, many=True).data,
            message='Successfully fetched all categories'
        )
    except Category.DoesNotExist:
        return api_response(
            success=False,
            status_code=status.HTTP_404_NOT_FOUND,
            errors='Category does not exist',
        )
    except Exception as e:
        print(e)
        return api_response(success=False, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message='Internal Server Error')


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_category(request):
    try:
        category = Category.objects.get(pk=request.GET.get('id'), is_active=True, is_deleted=False)
        return api_response(
            success=True,
            status_code=status.HTTP_200_OK,
            data=CategorySerializer(category).data,
        )
    except Category.DoesNotExist:
        return api_response(
            success=False,
            status_code=status.HTTP_404_NOT_FOUND,
            errors='Category does not exist',
        )
    except Exception as e:
        print(e)
        return api_response(success=False, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message='Internal Server Error')


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_all_products(request):
    try:
        products = Product.objects.all()

        for product in products:
            print(product.name, product.product_colors.all(), product.product_images.all())

        products = Product.objects.filter(is_active=True, is_deleted=False).all()
        return api_response(
            success=True,
            message='Successfully fetched all products',
            data=ProductSerializer(products, many=True).data,
            status_code=status.HTTP_200_OK,
        )
    except Product.DoesNotExist:
        return api_response(
            success=False,
            status_code=status.HTTP_404_NOT_FOUND,
            errors='Product does not exist',
        )

@api_view(['GET'])
@permission_classes((AllowAny,))
def get_product_by_id(request, pk):
    try:
        product = Product.objects.filter(pk=pk, is_active=True, is_deleted=False).first()
        # product_colors = ProductColorSerializer(ProductColor.objects.filter(product=product).all()).data
        # product_images = ProductImageSerializer(ProductImage.objects.filter(product=product).all()).data
        # print(product_colors)
        data = ProductDetailSerializer(product).data
        # data['product_colors'] = product_colors
        # data['product_images'] = product_images
        return api_response(
            success=True,
            message='Successfully fetched product',
            data=data,
            status_code=status.HTTP_200_OK,
        )
    except Product.DoesNotExist:
        return api_response(
            success=False,
            status_code=status.HTTP_404_NOT_FOUND,
            errors='Product does not exist',
        )