# Пример использования функций Map, Filter и Reduce:

# Допустим, у нас есть список чисел и мы хотим выполнить несколько операций над ними с помощью функций Map, Filter и Reduce.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Пример использования функции Map для возведения каждого элемента в квадрат
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Пример использования функции Filter для отбора только четных чисел
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # [2, 4, 6, 8, 10]

# Пример использования функции Reduce для нахождения суммы всех чисел
from functools import reduce
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers) # 55


# Основное отличие между функциями Map, Filter и Reduce заключается в том, что:

# Map - возвращает новый список, содержащий результаты применения заданной функции к каждому элементу входного списка.
# Filter - возвращает новый список, содержащий только элементы входного списка, которые удовлетворяют заданному условию.
# Reduce - используется для свертки входного списка до единственного значения, выполняя заданную функцию на парах 
# элементов списка и используя результат в качестве второго аргумента для следующего вызова функции.