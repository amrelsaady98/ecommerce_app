from django import forms
from django.contrib import admin
from rest_framework.exceptions import ValidationError

from products.models import Product, Category, ProductImage, ProductColor


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0
    max_num = 4

class ProductColorInline(admin.StackedInline):
    model = ProductColor
    extra = 0
    max_num = 3

class ProductAdminForm(forms.ModelForm):
    MAX_IMAGES = 4
    MAX_COLORS = 3

    class Meta:
        model = Product
        fields = '__all__'

    def clean_product_images(self):
        images = self.cleaned_data.get('product_images')
        if images and images.count() > self.MAX_IMAGES:
            raise ValidationError(f"You can only select up to {self.MAX_IMAGES} images.")
        return images

    def clean_product_colors(self):
        colors = self.cleaned_data.get('product_colors')
        if colors and colors.count() > self.MAX_COLORS:
            raise ValidationError(f"You can only select up to {self.MAX_COLORS} colors.")
        return colors

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Add other fields you want to display

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(ProductColor)
