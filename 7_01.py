# Ввод количества рек в словаре
n = int(input("Введите количество рек: "))

# Создание пустого словаря для хранения данных о реках и странах
rivers = {}

# Заполнение словаря данными о реках и странах
for i in range(n):
    country, *rivers_list = input().split()
    for river in rivers_list:
        rivers[river] = country

# Функция для вывода страны, в которой протекает указанная река
def find_country(river):
    if river in rivers:
        print(f"{river} протекает в стране {rivers[river]}")
    else:
        print(f"Река {river} не найдена")

# Функция для проверки наличия реки в словаре
def check_river(river):
    if river in rivers:
        print(f"Река {river} есть в словаре")
    else:
        print(f"Реки {river} нет в словаре")

# Функция для добавления новой пары страна-река в словарь
def add_river(river, country):
    rivers[river] = country

# Вывод словаря с данными о реках и странах
print(rivers)

# Поиск страны, в которой протекает указанная река
find_country("Нил")

# Проверка наличия реки в словаре
check_river("Амазонка")
check_river("Днепр")

# Добавление новой пары страна-река в словарь
add_river("Темза", "Великобритания")

# Вывод обновленного словаря с данными о реках и странах
print(rivers)
