# Напишите программу, используя минимум по 5 функции для работы с кортежем (tuple) и множествами (Set). 
# В виде данных пусть каждый студент предложит свое резюме. И будет работать с этими данными.

# Определение данных студентов в виде кортежа
student1 = ("Ali Zhetpis", 23, "Computer Science", "alizhetpis@example.com")
student2 = ("Makazhan Akazhanov", 19, "Mathematics", "makazhan@example.com")
student3 = ("Aisultan Kerimov", 21, "Biology", "aisultanker@example.com")

# Создание множества студентов
students = set([student1, student2, student3])

# Функция для получения списка имен студентов
def get_names(students):
    names = []
    for student in students:
        names.append(student[0])
    return names

# Функция для получения списка возрастов студентов
def get_ages(students):
    ages = []
    for student in students:
        ages.append(student[1])
    return ages

# Функция для получения списка электронных адресов студентов
def get_emails(students):
    emails = []
    for student in students:
        emails.append(student[3])
    return emails

# Функция для добавления нового студента в множество
def add_student(students, student):
    students.add(student)
    return students

# Функция для удаления студента из множества
def remove_student(students, student):
    students.remove(student)
    return students

# Получение списка имен студентов
names = get_names(students)
print("Names:", names)

# Получение списка возрастов студентов
ages = get_ages(students)
print("Ages:", ages)

# Получение списка электронных адресов студентов
emails = get_emails(students)
print("Emails:", emails)

# Добавление нового студента
new_student = ("Aigul Maigul", 18, "Computer Science", "aimai@example.com")
students = add_student(students, new_student)
print("После добавления:")
for student in students:
    print(student)

# Удаление студента
students = remove_student(students, student1)
print("После удаления:")
for student in students:
    print(student)
