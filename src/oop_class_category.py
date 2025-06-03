from itertools import product

from src.oop_class_product import Smartphone, Product, LawnGrass


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products) if products else 0
        Category.category_count += 1

    def __str__(self):
        total_count_products = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_count_products} шт."

    @property
    def products(self):
        products_info = []
        for product in self.__products:
            products_info.append(f"{product.name}, {product.price} руб., Остаток: {product.quantity} шт.")
        return '\n'.join(products_info)

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError