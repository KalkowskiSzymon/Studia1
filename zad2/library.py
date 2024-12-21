class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Biblioteka przy ul {self.street}, {self.city} {self.zip_code}. "
            f"Godziny Otwarcia: {self.open_hours} "
            f"Telefon : {self.phone} "
        )