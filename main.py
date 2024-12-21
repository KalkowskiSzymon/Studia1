from magazine import Product

product1 = Product.Product("Laptop", 1500)
product2 = Product.Product("Smartphone", 1000)

print(f"Cena przed rabatem: {product1.price}, {product2.price}")

product1.apply_discount(0.1)
product2.apply_discount(0.1)

print(f"Cena po rabacie: {product1.price}, {product2.price}")
