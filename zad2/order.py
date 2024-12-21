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
