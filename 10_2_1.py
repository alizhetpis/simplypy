string = input("Введите строку: ")

# Преобразуем строку в список символов
characters = list(string)

# Удаляем повторяющиеся символы из списка
unique_characters = list(set(characters))

# Сортируем список символов в алфавитном порядке
unique_characters.sort()

# Выводим на экран все уникальные символы в алфавитном порядке
print("Уникальные символы в строке:", end=" ")
for char in unique_characters:
    print(char, end=" ")


# Программа сначала считывает строку с клавиатуры и преобразует ее в список символов. 
# Затем она использует функцию set для удаления повторяющихся символов из списка и преобразует результат обратно в список с помощью функции list. 
# Далее программа сортирует список символов в алфавитном порядке с помощью метода sort. 
# Наконец, программа выводит на экран все уникальные символы в алфавитном порядке с помощью цикла for. 
# Обратите внимание на использование параметра end=" " в функции print, чтобы символы выводились через пробелы, а не на новых строках.