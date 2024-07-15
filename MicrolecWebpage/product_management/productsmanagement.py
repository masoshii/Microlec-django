from .models import Product, Brand, Category, Product_Category
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
import os

class ProductManager():
    @staticmethod
    def addproduct(name, brand, stock, price, image):
        id_product_brand = Brand.objects.filter(name_brand=brand).values_list('id_brand', flat=True)
        if id_product_brand:
            id_product_brand = id_product_brand[0]
            brand_instance = Brand.objects.get(id_brand=id_product_brand)
        else:
            return False, "Marca no encontrada."

        try:
            new_product = Product(name_product=name, id_brand=brand_instance, stock_product=stock, price_product=price, timestamp_product=timezone.now())
            new_product.save()

            extension = os.path.splitext(image.name)[1]

            filename = f"{new_product.id_product}{extension}"

            new_product.image_product.save(filename, image)
            
            new_product.save()
        
        except ValueError as ve:
            return False, f"Error en los tipos de valores: {ve}"
        except Exception as e:
            return False, f"Error desconocido: {e}"

        print(f"Se insertaron los siguientes datos: {name}, {id_product_brand}, {stock}, {price}, {timezone.now()}")
        return True, "Se han insertado los datos correctamente."

    @staticmethod
    def deleteproduct(product_id):
        if Product.objects.filter(id_product=product_id).exists():
            try:
                product_name = Product.objects.filter(id_product=product_id).values_list('name_product', flat=True)
                product_name = product_name[0]
                Product.objects.filter(id_product=product_id).delete()
                return True, f'El producto {product_name} se ha eliminado exitosamente.'
            except Exception as e:
                return False, e
        else:
            return False, "El producto no existe."

    @staticmethod
    def addbrand(brand_name):
        if Brand.objects.filter(name_brand=brand_name).exists():
            return False, f'La marca {brand_name} ya existe en el sistema.'
        else:
            try:
                new_brand = Brand(name_brand=brand_name)
                new_brand.save()
                return True, f'Se ha guardado la marca {brand_name} exitosamente.'
            except Exception as e:
                return False, e
    
    @staticmethod
    def deletebrand(brand_id):
        if Brand.objects.filter(id_brand=brand_id).exists():
            try:
                brand_name = Brand.objects.filter(id_brand=brand_id).values_list('name_brand', flat=True)
                brand_name = brand_name[0]
                Brand.objects.filter(id_brand=brand_id).delete()
                return True, f"La marca {brand_name} se ha eliminado exitosamente."
            except ValueError as ve:
                return False, f"Error en los tipos de valores: {ve}"
            except Exception as e:
                return False, e
        else:
            return False, "La marca especificada no existe."

    @staticmethod
    def addcategory(category_name):
        if Category.objects.filter(name_category=category_name).exists():
            return False, f'La categoria {category_name} ya existe en el sistema.'
        else:
            try:
                new_category = Category(name_category=category_name)
                new_category.save()
                return True, f'Se ha guardado la categoría {category_name} exitosamente.'
            except Exception as e:
                return False, e
    
    @staticmethod
    def deletecategory(category_id):
        if Category.objects.filter(id_category=category_id).exists():
            try:
                category_name = Category.objects.filter(id_category=category_id).values_list('name_category', flat=True)
                category_name = category_name[0]
                return True, f"La categoría {category_name} se ha eliminado exitosamente."
            except ValueError as ve:
                return False, f"Error en los tipos de valores: {ve}"
            except Exception as e:
                return False, e
        else:
            return False, "La categoría especificada no existe."
    
    @staticmethod
    def addcategorytoproduct(product_id, category_id):
        if Category.objects.filter(id_category=category_id).exists():
            if Product.objects.filter(id_product=product_id).exists():
                category_instance = Category.objects.get(id_category=category_id)
                product_instance = Product.objects.get(id_product=product_id)
                product_name = Product.objects.filter(id_product=product_id).values_list('name_product', flat=True)
                product_name = product_name[0]
                category_name = Category.objects.filter(id_category=category_id).values_list('name_category', flat=True)
                category_name = category_name[0]
                try:
                    new_productcategory = Product_Category(id_category=category_instance, id_product=product_instance)
                    new_productcategory.save()
                except ValueError as ve:
                    return False, f"Error en los tipos de valores: {ve}"
                except Exception as e:
                    return False, e
            else:
                return False, "El producto especificado no existe."
        else:
            return False, "La categoría especificada no existe."
        return True, f"Se le ha añadido la categoría {category_name} al producto {product_name} exitosamente"

    @staticmethod
    def removecategoryfromproduct(product_id, category_id):
        if Category.objects.filter(id_category=category_id).exists():
            if Product.objects.filter(id_product=product_id).exists():
                category_name = Category.objects.filter(id_category=category_id).values_list('name_category', flat=True)
                category_name = category_name[0]
                product_name = Product.objects.filter(id_product=product_id).values_list('name_product', flat=True)
                product_name = product_name[0]
                try:
                    Product_Category.objects.filter(id_product=product_id, id_category=category_id).delete()
                except ValueError as ve:
                    return False, f"Error en los tipos de valores: {ve}"
                except Exception as e:
                    return False, e
            else:
                return False, "El producto especificado no existe."
        else:
            return False, "La categoría especificada no existe."
        return True, f"Se ha sacado la categoría {category_name} del producto {product_name} exitosamente."




