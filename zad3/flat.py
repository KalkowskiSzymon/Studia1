from zad3.property import Property


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
