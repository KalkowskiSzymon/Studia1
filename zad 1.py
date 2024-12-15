class Student:
    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def is_passed(self):

        if not self.marks: 
            return False
        average = sum(self.marks) / len(self.marks)
        return average > 50

student1 = Student("Alice", [60, 70, 80])  
student2 = Student("Bob", [40, 30, 20])    

print(f"Czy {student1.name} zdał(a)? {student1.is_passed()}") 
print(f"Czy {student2.name} zdał(a)? {student2.is_passed()}") 