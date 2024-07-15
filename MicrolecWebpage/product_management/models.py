from django.db import models

class Brand(models.Model):
    id_brand = models.BigAutoField(primary_key=True, null=False)
    name_brand = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name_brand
     
class Category(models.Model):
    id_category = models.BigAutoField(primary_key=True, null=False)
    name_category = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name_category
    
class Product(models.Model):
    id_product = models.BigAutoField(primary_key=True, null=False)
    name_product = models.CharField(max_length=200, null=False)
    id_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock_product = models.IntegerField(null=False)
    price_product = models.IntegerField(null=False)
    timestamp_product = models.DateTimeField(null=False)
    image_product = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name_product

class Product_Category(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_product
    


