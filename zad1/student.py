class Student:
    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def is_passed(self):

        if not self.marks:
            return False
        average = sum(self.marks) / len(self.marks)
        return average > 50
