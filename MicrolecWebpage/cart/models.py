from django.db import models
from product_management.models import Product
from user_management.models import User


class CartModel(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return self.id_user
