# Напишите программу, в которой предлагается вводить учащихся различных групп, посещающих секции по разным предметам. 
# Требуется упорядочить  список  по различным  категориям. Вывести  результат  на экран. 

students = []

def add_student(name, group, subject):
    student = {"name": name, "group": group, "subject": subject}
    students.append(student)

def sort_students_by_group():
    return sorted(students, key=lambda x: x["group"])

def sort_students_by_subject():
    return sorted(students, key=lambda x: x["subject"])

def print_students(sorted_students):
    for student in sorted_students:
        print("Name: {}, Group: {}, Subject: {}".format(student["name"], student["group"], student["subject"]))

while True:
    name = input("Enter student name (or enter 'q' to quit): ")
    if name == 'q':
        break
    group = input("Enter student group: ")
    subject = input("Enter subject attended by student: ")
    add_student(name, group, subject)

print("\nSorted by group:")
sorted_by_group = sort_students_by_group()
print_students(sorted_by_group)

print("\nSorted by subject:")
sorted_by_subject = sort_students_by_subject()
print_students(sorted_by_subject)
