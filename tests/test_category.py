def test_category(category_smph, category_gls):
    assert category_smph.name == "Смартфоны"
    assert category_smph.description == "Высокотехнологичные смартфоны"
    assert category_gls.name == "Газонная трава"
    assert category_gls.description == "Различные виды газонной травы"
    # assert category_gls.products == []
    # assert category_smph.products == [smartphone1, smartphone2]


def test_add_product(add_products1, add_products2, add_products3, add_products4):
    assert add_products1 == "Samsung Galaxy S23 Ultra, 180000.0 руб., Остаток: 5 шт."
    assert add_products2 == "Iphone 15, 210000.0 руб., Остаток: 8 шт."
    assert add_products3 == "Xiaomi Redmi Note 11, 31000.0 руб., Остаток: 14 шт."
    assert add_products4 == "Возникла ошибка TypeError при добавлении не продукта"
