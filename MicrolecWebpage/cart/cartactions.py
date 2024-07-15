from product_management.models import Product
from user_management.models import User
from .models import CartModel

class CartAction():

    @staticmethod
    def add_cart_item(product_instance, user_instance, quantity=1):
        try:
            cart_item = CartModel.objects.get(id_user=user_instance, id_product=product_instance)
            cart_item.quantity += quantity
            cart_item.save()
        except CartModel.DoesNotExist:
            cart_item = CartModel.objects.create(id_user=user_instance, id_product=product_instance, quantity=quantity)
        
        return cart_item
        