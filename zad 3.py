class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (
            f"Nieruchomość położona pod adresem {self.address} "
            f"z {self.rooms} pokojami, "
            f"obejmujący obszar {self.area} m2 , w cenie {self.price}."
        )


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"Dom przy ulicy {self.address} z {self.rooms} pokojami, "
            f"obejmujący obszar  {self.area} m2 , w cenie {self.price}. "
            f"Nieruchomość składa się z działki o poweirzchni {self.plot} m2."
        )


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"Mieszkanie zlokalizowane pod adresem {self.address} "
            f"na piętrze {self.floor}, "
            f"z {self.rooms} pokojami, o powierzchni {self.area} m2, "
            f"wyceniony na {self.price}."
        )


house = House(
    area=200,
    rooms=5,
    price=500000,
    address="Kostromska 78",
    plot=800)
flat = Flat(
    area=80,
    rooms=3,
    price=200000,
    address="Słowackiego 44",
    floor=4)

print(house)
print(flat)
