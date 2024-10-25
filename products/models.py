from django.db import models

class Category(models.Model):
    # Primary key, auto-incremented by default
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)  # Use max_length to specify the varchar length
    description = models.TextField(blank=True, null=True)  # Use TextField for longer text
    icon_image = models.ImageField(upload_to='category_icons/', blank=True, null=True)  # Specify upload path
    is_active = models.BooleanField(default=True)  # Default to active
    is_deleted = models.BooleanField(default=False)  # Default to not deleted

    def __str__(self):
        return self.name  # String representation of the model

    class Meta:
        verbose_name_plural = "Categories"