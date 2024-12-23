# Generated by Django 5.1.2 on 2024-10-30 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_remove_product_product_colors_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_colors',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='products.productcolor'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_images',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='products.productimage'),
        ),
    ]
