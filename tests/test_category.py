def test_category(category_1, product_1, product_2, product_3):
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_1.product_count == 3

    assert category_1.products == ('Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.// Iphone 15, 210000.0 '
 'руб. Остаток: 8 шт.// Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.')
