def test_category(category_1, product_1, product_2, product_3):
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_1.product_count == 3

    assert len(category_1.products) == 146
