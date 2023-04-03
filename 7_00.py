# Создание пустого словаря для хранения данных студентов
students = {}

# Функция добавления данных студента в словарь
def add_student(name, resume):
    students[name] = resume

# Функция удаления данных студента из словаря
def remove_student(name):
    if name in students:
        del students[name]
    else:
        print(f"Студент {name} не найден")

# Функция поиска данных студента в словаре
def find_student(name):
    if name in students:
        print(students[name])
    else:
        print(f"Студент {name} не найден")

# Функция вывода всех данных о студентах
def print_all_students():
    for name, resume in students.items():
        print(f"{name}: {resume}")

# Функция изменения данных студента в словаре
def update_student(name, resume):
    if name in students:
        students[name] = resume
    else:
        print(f"Студент {name} не найден")

# Добавление данных студентов в словарь
add_student("Иванов", "Опытный программист с 5-летним стажем, владеющий языками Python, Java и C++. Опыт работы с базами данных и фреймворками Django и Flask")
add_student("Петров", "Студент-программист с опытом работы в разработке веб-приложений на Python. Владеет также языками Java и JavaScript")

# Поиск и вывод данных студента
find_student("Иванов")

# Изменение данных студента
update_student("Петров", "Опытный веб-разработчик с опытом работы в проектах на Python, Java и JavaScript")

# Вывод всех данных о студентах
print_all_students()

# Удаление данных студента
remove_student("Иванов")

# Вывод всех данных о студентах после удаления
print_all_students()
