# Вводятся имена студентов в одну строку через пробел. На их основе формируется кортеж. 
# Отобразите на экране все имена из этого кортежа, которые содержат фрагмент "ва". 
# Имена выводятся в одну строку через пробел.

# Вводим имена студентов через пробел и разбиваем строку на отдельные имена
names = input("Введите имена студентов через пробел: ").split()

# Создаем пустой список для имен, содержащих фрагмент "ва"
selected_names = []

# Проходим по каждому имени и проверяем, содержит ли оно фрагмент "ва"
for name in names:
    if "ва" in name:
        selected_names.append(name)
        print("Имена, содержащие 'ва':", " ".join(selected_names))
    else:
        print("Нет имен")

