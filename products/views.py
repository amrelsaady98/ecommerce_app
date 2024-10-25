from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from core.utils import api_response
from products.models import Category
from products.serializers import CategorySerializer


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

