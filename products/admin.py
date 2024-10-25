from django.contrib import admin

from products.models import Product, Category, ProductImage, ProductColor


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0
    max_num = 4

class ProductColorInline(admin.StackedInline):
    model = ProductColor
    extra = 0
    max_num = 3

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductColorInline]  # Add the inline to the Product admin
    list_display = ('name',)  # Add other fields you want to display

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(ProductColor)
