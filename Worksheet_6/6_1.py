import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = {
    'Student Name': ['Arin', 'Aditya', 'Chirag', 'Gurleen', 'Kunal'],
    'Math': [85, 79, 90, 66, 70],
    'Physics': [78, 82, 85, 75, 68],
    'Chemistry': [92, 74, 89, 80, 75],
    'English': [88, 90, 92, 78, 85]}
subjects = ['Math', 'Physics', 'Chemistry', 'English']
marks = np.array([data[subject] for subject in subjects])
students = np.array(data['Student Name'])
total_marks = np.sum(marks, axis=0)
average_marks = np.mean(marks, axis=0)
for i, student in enumerate(students):
    print(f"{student} - Total: {total_marks[i]}")
    print(f"Average: {total_marks[i] / len(subjects)}")
top_performer = students[np.argmax(total_marks)]
bottom_performer = students[np.argmin(total_marks)]
print(f"Top Performer: {top_performer}")
print(f"Bottom Performer: {bottom_performer}")
pass_marks = 80
passed_students = np.sum(np.all(marks >= pass_marks, axis=0))
passing_percentage = (passed_students / len(students)) * 100

print(f"Passing Percentage: {passing_percentage}%")
for i, subject in enumerate(subjects):
    plt.figure()
    plt.bar(students, marks[i])
    plt.title(f'Student Performance in {subject}')
    plt.xlabel('Students')
    plt.ylabel('Marks')
    plt.show()
    subject_averages = np.mean(marks, axis=1)

plt.bar(subjects, subject_averages)
plt.title('Average Marks Across Subjects')
plt.xlabel('Subjects')
plt.ylabel('Average Marks')
plt.show()