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


class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Pracownik: {self.first_name} {self.last_name} "
            f"Data wynajmu: {self.hire_date} "
            f"Data urodzenia: {self.birth_date} "
            f"Adres: {self.street}, {self.city}, {self.zip_code} "
            f"Telefon kontaktowy: {self.phone} "
        )


class Book:
    def __init__(
        self, library,
        publication_date,
        author_name,
        author_surname,
        number_of_pages
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Autor {self.author_name} {self.author_surname}, "
            f"Data publikacji: {self.publication_date}, "
            f"Stron: {self.number_of_pages}, Dostępna w: {self.library}"
        )


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n    ".join(str(book) for book in self.books)
        return (
            f"Data zamówienia: {self.order_date}, "
            f"Przetworzone przez: {self.employee}, Uczeń: {self.student}\n "
            f"Książki w porządku:\n    {books_str} "
        )


library1 = Library(
    "Warszawa",
    "Armii Krajowej 29",
    "00-001",
    "9:00 - 17:00",
    "+48 22 123 45 67"
)

library2 = Library(
    "Kraków",
    "Wojska Polskiego 10",
    "31-042",
    "10:00 - 18:00",
    "+48 12 765 43 21"
)

book1 = Book(library1, "2020-01-15", "J.K.", "Rowling", 400)
book2 = Book(library1, "1999-07-08", "J.R.R.", "Tolkien", 310)
book3 = Book(library2, "2015-03-12", "George", "Orwell", 328)
book4 = Book(library2, "2021-11-11", "Haruki", "Murakami", 420)
book5 = Book(library1, "2000-05-01", "Gabriel", "Garcia Marquez", 360)

employee1 = Employee(
    "Anna",
    "Kowalska",
    "2021-09-01",
    "1990-04-15",
    "Warszawa",
    "Grodzka 8",
    "00-002",
    "+48 22 555 44 33",
)
employee2 = Employee(
    "Jan",
    "Nowak",
    "2020-03-15",
    "1985-07-22",
    "Kraków",
    "Kujawska 89",
    "31-043",
    "+48 12 123 45 67",
)
employee3 = Employee(
    "Maria",
    "Wiśniewska",
    "2018-11-30",
    "1992-02-10",
    "Warszawa",
    "Szkolna 13",
    "00-003",
    "+48 22 678 90 12",
)

student1 = "Tomasz Zielinski"
student2 = "Katarzyna Nowak"
student3 = "Piotr Kowalczyk"

order1 = Order(employee1, student1, [book1, book2], "2024-12-01")
order2 = Order(employee2, student2, [book3, book4, book5], "2024-12-10")

print(order1)
print(order2)
