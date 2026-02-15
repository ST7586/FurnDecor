from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=100)

    features = models.TextField(blank=True)
    details = models.TextField(blank=True)
    product_care = models.TextField(blank=True)
    return_policy = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    seater = models.CharField(max_length=20, null=True, blank=True)   # single, two, three
    price = models.IntegerField()
    old_price = models.IntegerField()
    discount = models.IntegerField()
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return f"{self.product.name} - {self.seater}"


class Wishlist(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class CartItem(models.Model):
    session_key = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    variant_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="cart/")
    new_price = models.IntegerField()
    old_price = models.IntegerField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
