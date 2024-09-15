class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None

    def set_student_class(self, student_class):
        self.student_class = student_class

    def display_attributes(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Class: {self.student_class}")

student1 = Student(102323050, "Aditya")

student1.set_student_class("2nd Year")

student1.display_attributes()
