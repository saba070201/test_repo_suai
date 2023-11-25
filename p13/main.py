# 1
class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
       


class Buyer:
    def __init__(self, name,balance) -> None:
        self.name = name
        self.balance = balance

class ProductCard:
    def __init__(self, buyer, products: Product) -> None:
        self.products = products
        self.buyer = buyer

    def get_total_price(self):
        tp = 0
        for i in self.products:
            tp += i.price
        return tp
    # или так 
    @property
    def total_price(self):
        tp = 0
        for i in self.products:
            tp += i.price
        return tp 


class Order:
    def __init__(self, product_card: ProductCard) -> None:
        self.product_card = product_card
        self.is_closed = False

    def close_order(self):
        if self.product_card.buyer.balance > self.product_card.get_total_price():
            self.is_closed = True
        return {"success": True}


# 2
import abc


class Technique(abc.ABC):
    @abc.abstractmethod
    def get_energy(self):
        pass

    @abc.abstractmethod
    def waste_energy(self):
        pass


class Car(Technique):
    def get_energy(self):
        return super().get_energy()

    def waste_energy(self):
        return super().waste_energy()


class AirPlane(Technique):
    def get_energy(self):
        return super().get_energy()

    def waste_energy(self):
        return super().waste_energy()


# 3
class Charter(abc.ABC):
    @abc.abstractmethod
    def attack(self):
        pass

    @abc.abstractmethod
    def get_damage(self):
        pass


class BaseWeapon(abc.ABC):
    @abc.abstractmethod
    def add_damage_to_base(self):
        pass


class BaseArmor(abc.ABC):
    @abc.abstractmethod
    def subtract_damage(self):
        pass


class NegativeDamage(Exception):
    def __init__(self, message, value) -> None:
        self.message = message
        self.value = value
        if self.value <= 0:
            raise self

    def __str__(self) -> str:
        return f"{self.message}"


class NegativeHealth(Exception):
    def __init__(self, message, value) -> None:
        self.message = message
        self.value = value
        if self.value <= 0:
            raise self

    def __str__(self) -> str:
        return f"{self.message}"
nh=NegativeHealth('плохо',10)