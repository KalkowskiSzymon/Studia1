from zad3.property import Property


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
