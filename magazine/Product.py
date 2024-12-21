from magazine import utils


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, discount):
        self.price = utils.calculate_discount(self.price, discount)
        return self.price
