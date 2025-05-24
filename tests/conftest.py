import pytest

from src.oop_class_category import Category
from src.oop_class_product import Product


# Фикстуры для class Product
@pytest.fixture
def product_1():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def product_2():
    return Product(
        name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8
    )


@pytest.fixture
def product_3():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )

@pytest.fixture
def sum_1(product_1, product_2):
    return 2580000.0

@pytest.fixture
def sum_2(product_1, product_3):
    return 1334000.0

@pytest.fixture
def sum_3(product_2, product_3):
    return 2114000.0

# # Фикстуры для class Category
# @pytest.fixture
# def category_1(product_1, product_2, product_3):
#     return Category(
#         name="Смартфоны",
#         description="Смартфоны, как средство не только коммуникации, "
#         "но и получения дополнительных функций для удобства жизни",
#         products=[product_1, product_2, product_3],
#     )
