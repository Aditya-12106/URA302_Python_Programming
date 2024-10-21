import numpy as np

students_data = {
    'Arin': [85, 78, 92, 88],
    'Aditya': [79, 82, 74, 90],
    'Chirag': [90, 85, 89, 92],
    'Gurleen': [66, 75, 80, 78],
    'Kunal': [70, 68, 75, 85]
}

subjects = ['Math', 'Physics', 'Chemistry', 'English']

total_marks = {name: sum(marks) for name, marks in students_data.items()}
average_marks = {name: round(float(np.mean(marks)), 2) for name, marks in students_data.items()}

subject_wise_performance = {subject: round(float(np.mean([students_data[name][i] for name in students_data])), 2) for i, subject in enumerate(subjects)}

top_performer = max(total_marks, key=total_marks.get)
bottom_performer = min(total_marks, key=total_marks.get)

passing_students = sum(all(mark >= 80 for mark in marks) for marks in students_data.values())
passing_percentage = (passing_students / len(students_data)) * 100

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Subject-wise Performance (Average):", subject_wise_performance)
print(f"Top Performer: {top_performer} with {total_marks[top_performer]} total marks")
print(f"Bottom Performer: {bottom_performer} with {total_marks[bottom_performer]} total marks")
print(f"Passing Percentage: {passing_percentage}%")