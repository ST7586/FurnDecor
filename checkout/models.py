# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    variant_id = models.IntegerField()
    product_name = models.CharField(max_length=200)
    price = models.FloatField()

    mobile = models.CharField(max_length=15)
    pincode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.TextField()

    payment_method = models.CharField(max_length=50)
    is_paid = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
