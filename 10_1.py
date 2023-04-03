# Пример программы, в которой 10 встроенных функций связаны друг с другом и имеют логическое начало и конец:

import random
import math
import string

# Функция, которая генерирует случайный пароль заданной длины
def generate_password(length):
    # Список символов, из которых будем формировать пароль
    characters = string.ascii_letters + string.digits + string.punctuation

    # Генерируем случайный пароль заданной длины
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Функция, которая проверяет, является ли число простым
def is_prime(number):
    # Проверяем, является ли число 2 или 3
    if number == 2 or number == 3:
        return True

    # Если число меньше 2 или кратно 2 или 3, то оно не является простым
    if number < 2 or number % 2 == 0 or number % 3 == 0:
        return False

    # Проверяем, делится ли число на другие числа от 3 до sqrt(number) без остатка
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False

    # Если число не делится на другие числа от 3 до sqrt(number), то оно является простым
    return True

# Функция, которая находит первые n простых чисел
def find_primes(n):
    primes = []
    number = 2
    while len(primes) < n:
        if is_prime(number):
            primes.append(number)
        number += 1
    return primes

# Функция, которая генерирует случайное целое число в заданном диапазоне
def generate_random_number(min, max):
    return random.randint(min, max)

# Функция, которая находит сумму всех элементов списка
def calculate_sum(numbers):
    return sum(numbers)

# Функция, которая находит среднее значение всех элементов списка
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Функция, которая находит максимальный элемент списка
def find_max(numbers):
    return max(numbers)

# Функция, которая находит минимальный элемент списка
def find_min(numbers):
    return min(numbers)

# Функция, которая находит длину строки
def calculate_string_length(string):
    return len(string)

# Функция, которая находит количество вхождений подстроки в строку
def count_substring_occurrences(string, substring):
    return string.count(substring)

# Пример использования всех функций:
password = generate_password(8)
print("Сгенерированный пароль:", password)

primes = find_primes(10)
print("Первые 10 простых чисел:", primes)

random_number = generate_random_number(1, 100)
print("Случайное число в диапазоне от 1 до 100:", random_number)

numbers = [3, 5, 7, 2, 8, 4, 1, 6, 9]
print("Список чисел:", numbers)

sum_numbers = calculate_sum(numbers)
print("Сумма всех чисел в списке:", sum_numbers)

average = calculate_average(numbers)
print("Среднее значение всех чисел в списке:", average)

max_number = find_max(numbers)
print("Максимальное число в списке:", max_number)

min_number = find_min(numbers)
print("Минимальное число в списке:", min_number)

string = "Hello, world!"
print("Строка:", string)

string_length = calculate_string_length(string)
print("Длина строки:", string_length)

substring = "l"
substring_count = count_substring_occurrences(string, substring)
print("Количество вхождений подстроки '" + substring + "' в строку:", substring_count)


# В этой программе мы использовали 10 встроенных функций:

# - `random.choice` - выбирает случайный элемент из списка
# - `math.sqrt` - находит квадратный корень числа
# - `string.ascii_letters` - строка, содержащая все буквы алфавита (в верхнем и нижнем регистре)
# - `string.digits` - строка, содержащая все цифры
# - `string.punctuation` - строка, содержащая все знаки пунктуации
# - `sum` - находит сумму всех элементов списка
# - `len` - находит длину списка или строки
# - `max` - находит максимальный элемент списка
# - `min` - находит минимальный элемент списка
# - `count` - находит количество вхождений подстроки в строку

# Вся программа имеет логическое начало (генерация случайного пароля и простых чисел) и 
# логический конец (нахождение длины строки и количества вхождений подстроки в строку). 
# Все функции связаны между собой таким образом, что результаты работы одной функции могут использоваться в других функциях. 
# Например, случайное число, сгенерированное функцией `generate_random_number`, 
# может быть использовано для выбора случайного элемента списка в функции `calculate_sum`.

