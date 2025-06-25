import pytest


def test_product(smph1, smph2, smph3, gls1, gls2):
    assert smph1.name == "Samsung Galaxy S23 Ultra"
    assert smph1.description == "256GB, Серый цвет, 200MP камера"
    assert smph1.price == 180000.0
    assert smph1.quantity == 5
    assert smph1.efficiency == 95.5
    assert smph1.model == "S23 Ultra"
    assert smph1.memory == 256
    assert smph1.color == "Серый"

    assert smph2.name == "Iphone 15"
    assert smph2.description == "512GB, Gray space"
    assert smph2.price == 210000.0
    assert smph2.quantity == 8
    assert smph2.efficiency == 98.2
    assert smph2.model == "15"
    assert smph2.memory == 512
    assert smph2.color == "Gray space"

    assert smph3.name == "Xiaomi Redmi Note 11"
    assert smph3.description == "1024GB, Синий"
    assert smph3.price == 31000.0
    assert smph3.quantity == 14
    assert smph3.efficiency == 90.3
    assert smph3.model == "Note 11"
    assert smph3.memory == 1024
    assert smph3.color == "Синий"

    assert gls1.name == "Газонная трава"
    assert gls1.description == "Элитная трава для газона"
    assert gls1.price == 500.0
    assert gls1.quantity == 20
    assert gls1.country == "Россия"
    assert gls1.germination_period == "7 дней"
    assert gls1.color == "Зеленый"

    assert gls2.name == "Газонная трава 2"
    assert gls2.description == "Выносливая трава"
    assert gls2.price == 450.0
    assert gls2.quantity == 15
    assert gls2.country == "США"
    assert gls2.germination_period == "5 дней"
    assert gls2.color == "Темно-зеленый"


def test_add(sum_smph_1, sum_gls_1, sum_type_error):
    assert sum_smph_1 == 2580000.0
    assert sum_gls_1 == 16750.0
    assert sum_type_error == "Возникла ошибка TypeError при попытке сложения"
