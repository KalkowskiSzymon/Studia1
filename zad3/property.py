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
