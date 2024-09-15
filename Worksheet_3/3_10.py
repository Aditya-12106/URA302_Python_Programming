class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

student1 = Student(student_id="102323050", student_name="Aditya", student_class="2W12")
student2 = Student(student_id="102315220", student_name="Andy", student_class="2E22")

print("Student1:")
print(f"Student ID: {student1.student_id}")
print(f"Name: {student1.student_name}")
print(f"Class: {student1.student_class}")

print("\nStudent2:")
print(f"Student ID: {student2.student_id}")
print(f"Name: {student2.student_name}")
print(f"Class: {student2.student_class}")