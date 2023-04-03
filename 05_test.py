# 1.	Напишите функцию создания списка из чисел от 0 до N (N – аргумент функции), выведите значение каждого элемента в консоль.

#print(list(range(int(input("Enter N: ")))))

# def create_list(N):
#     for i in range(N + 1):
#         print(i)

# N = int(input("Enter N: "))
# create_list(N)


# 2.	Перепишите функцию так, что в зависимости от значения формального (дефолтного) параметра type, функция будет преобразовывать список в кортеж. 
#       (type=None значит список остаётся списком, значение type='t' то список преобразуется в кортеж)

# def convert_list(l):
#     a = []
#     typea = type(a)

#     if type(l) == typea:
#         tpl = tuple(l)
#         print('t')
#     else:
#         print('None')

# n = (1,2,3,4,5)
# convert_list(n)

# 3.	Напишите декоратор, замеряющий скорость работы функции, при "чтении" кортежа и "чтении" списка. 
#       (посмотрите при каких значениях N функция с преобразованием списка в кортеж работает быстрее, 
#       в теории кортеж 'читается' быстрее, но на преобразование тоже уходит время)

import time

def speed_measure_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start}")
        return result
    return wrapper

@speed_measure_decorator
def read_list_or_tuple(input_data):
    for i in input_data:
        pass

input_list = list(range(100000))
input_tuple = tuple(range(100000))

print("Reading list:")
read_list_or_tuple(input_list)
print("Reading tuple:")
read_list_or_tuple(input_tuple)
