from products import views
from django.urls import path

urlpatterns = [
    path('categories/all/', views.get_all_categories, name='get_all_categories'),
    path('categories/', views.get_category, name='get_category_by_id'),
]