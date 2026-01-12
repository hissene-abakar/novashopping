from django.db import models
from category.models import Category
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="products/")
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE
    )
# Create your models here.
