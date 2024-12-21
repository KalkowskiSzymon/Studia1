from magazine import utils


class Order:
    def __init__(self, products):
        self.products = products

    def total_price(self):
        return sum(product.price for product in self.products)

    def apply_discount(self, discount):
        for product in self.products:
            product.apply_discount(discount)
