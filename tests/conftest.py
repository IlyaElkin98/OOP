import pytest

from src.oop_class_category import Category
from src.oop_class_product import Product, Smartphone, LawnGrass


# Фикстуры для class Product
@pytest.fixture
def smph1():
    return Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый",
    )


@pytest.fixture
def smph2():
    return Smartphone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space",
    )


@pytest.fixture
def smph3():
    return Smartphone(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
        efficiency=90.3,
        model="Note 11",
        memory=1024,
        color="Синий",
    )


@pytest.fixture
def gls1():
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )


@pytest.fixture
def gls2():
    return LawnGrass(
        name="Газонная трава 2",
        description="Выносливая трава",
        price=450.0,
        quantity=15,
        country="США",
        germination_period="5 дней",
        color="Темно-зеленый",
    )


@pytest.fixture
def sum_smph_1(smph1, smph2):
    return 2580000.0


@pytest.fixture
def sum_gls_1(gls1, gls2):
    return 16750.0


@pytest.fixture
def sum_type_error(smph1, gls1):
    return "Возникла ошибка TypeError при попытке сложения"


# Фикстуры для class Category
@pytest.fixture
def add_products1(smph1):
    return f"{smph1.name}, {smph1.price} руб., Остаток: {smph1.quantity} шт."


@pytest.fixture
def add_products2(smph2):
    return f"{smph2.name}, {smph2.price} руб., Остаток: {smph2.quantity} шт."


@pytest.fixture
def add_products3(smph3):
    return f"{smph3.name}, {smph3.price} руб., Остаток: {smph3.quantity} шт."


@pytest.fixture
def add_products4():
    return "Возникла ошибка TypeError при добавлении не продукта"


@pytest.fixture
def category_smph():
    return Category(
        name="Смартфоны", description="Высокотехнологичные смартфоны", products=[]
    )


@pytest.fixture
def category_gls():
    return Category(
        name="Газонная трава", description="Различные виды газонной травы", products=[]
    )
