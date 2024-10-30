from django.db import models

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    icon_image = models.ImageField(upload_to='category_icons/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class ProductImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='product_images/')
    order = models.IntegerField(default=0)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.product.__str__() + "image number " + str(self.order)

class ProductColor(models.Model):
    color_id = models.AutoField(primary_key=True)
    color = models.CharField(max_length=255, default='#FFFFFF')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='colors')

    def __str__(self):
        return self.color

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=255)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image1 = models.ImageField(upload_to='product_icons/', blank=True, null=True)
    name = models.CharField(max_length=255)
    our_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    has_discount = models.BooleanField(default=False, blank=True, null=True)
    total_rating = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock_qty = models.IntegerField()
    year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    product_images = models.ManyToManyField(ProductImage, related_name='products', blank=True, null=True)
    product_colors = models.ManyToManyField(ProductColor, related_name='products', blank=True, null=True)





    def __str__(self):
        return self.name






