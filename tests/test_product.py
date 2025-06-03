import pytest


def test_product(product_1, product_2, product_3):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5

    assert product_2.name == "Iphone 15"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 210000.0
    assert product_2.quantity == 8

    assert product_3.name == "Xiaomi Redmi Note 11"
    assert product_3.description == "1024GB, Синий"
    assert product_3.price == 31000.0
    assert product_3.quantity == 14

def test_str_product(product_1, product_2, product_3):
    assert f"{product_1.name}, {product_1.price} руб. Остаток: {product_1.quantity} шт." == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert f"{product_2.name}, {product_2.price} руб. Остаток: {product_2.quantity} шт." == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert f"{product_3.name}, {product_3.price} руб. Остаток: {product_3.quantity} шт." == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."

def test_add(product_1, product_2, product_3, sum_1, sum_2, sum_3):
    assert sum_1 == 2580000.0
    assert sum_2 == 1334000.0
    assert sum_3 == 2114000.0