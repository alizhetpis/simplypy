students = []

def add_student(name, group, subject):
    student = {'name': name, 'group': group, 'subject': subject}
    students.append(student)

def remove_student(name):
    for i, student in enumerate(students):
        if student['name'] == name:
            del students[i]
            break

def sort_by_name():
    students.sort(key=lambda x: x['name'])

def sort_by_group():
    students.sort(key=lambda x: x['group'])

def sort_by_subject():
    students.sort(key=lambda x: x['subject'])

def display_students():
    for student in students:
        print(student['name'], student['group'], student['subject'])

while True:
    print("""
    1. Add student
    2. Remove student
    3. Sort by name
    4. Sort by group
    5. Sort by subject
    6. Display students
    0. Quit
    """)

    choice = int(input("Enter your choice: "))
    if choice == 0:
        break
    elif choice == 1:
        name = input("Enter name: ")
        group = input("Enter group: ")
        subject = input("Enter subject: ")
        add_student(name, group, subject)
    elif choice == 2:
        name = input("Enter name: ")
        remove_student(name)
    elif choice == 3:
        sort_by_name()
    elif choice == 4:
        sort_by_group()
    elif choice == 5:
        sort_by_subject()
    elif choice == 6:
        display_students()
