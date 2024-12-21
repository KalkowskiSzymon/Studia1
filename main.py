from zad1.student import Student
from zad2.book import Book
from zad2.employee import Employee
from zad2.library import Library
from zad2.order import Order
from zad3.flat import Flat
from zad3.house import House

student1 = Student("Alice", [60, 70, 80])
student2 = Student("Bob", [40, 30, 20])

print(f"Czy {student1.name} zdał(a)? {student1.is_passed()}")
print(f"Czy {student2.name} zdał(a)? {student2.is_passed()}")


library1 = Library(
    "Warszawa", "Armii Krajowej 29", "00-001", "9:00 - 17:00", "+48 22 123 45 67"
)

library2 = Library(
    "Kraków", "Wojska Polskiego 10", "31-042", "10:00 - 18:00", "+48 12 765 43 21"
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

house = House(area=200, rooms=5, price=500000, address="Kostromska 78", plot=800)

flat = Flat(area=80, rooms=3, price=200000, address="Słowackiego 44", floor=4)

print(house)
print(flat)
