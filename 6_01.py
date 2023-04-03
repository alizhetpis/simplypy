# Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно.
# Заполните второй кортеж числами от -5 до 0.
# Для заполнения кортежей числами напишите одну функцию.
# Объедините два кортежа с помощью оператора +, создав тем самым третий кортеж.
# С помощью метода кортежа count() определите в нем количество нулей.
# Выведите на экран третий кортеж и количество нулей в нем.

import random

def create_random_tuple(start, end, length):
    return tuple(random.randint(start, end) for _ in range(length))

first_tuple = create_random_tuple(0, 5, 10)
print("Первый кортеж: ", first_tuple)
second_tuple = create_random_tuple(-5, 0, 10)
print("Второй кортеж: ", second_tuple)

third_tuple = first_tuple + second_tuple
num_zeros = third_tuple.count(0)

print("Третий кортеж: ", third_tuple)
print("Количество нулей в третьем кортеже: ", num_zeros)
