from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __add__(self, other):
        """Метод сложения цены и количества определенного продукта"""
        pass


class MixinPrint:
    def __init__(self, *args, **kwargs) -> None:
        print(repr(self))

    def __repr__(self):
        """метод возвращающий человечное представление экземпляра класса (конкретного продукта)"""
        return f"Название продукта: {self.name}, Описание продукта: {self.description}, Цена: {self.price}, Остаток: {self.quantity}"


class Product(BaseProduct, MixinPrint):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        if quantity != 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __add__(self, other):
        pass


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
