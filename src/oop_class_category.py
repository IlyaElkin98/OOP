from src.oop_class_product import Product


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

    def middle_price(self):
        """Метод подчёта среднего ценника"""
        try:
            return round(sum(product.price for product in self.__products)/len(self.__products), 2)
        except ZeroDivisionError:
            return 0

