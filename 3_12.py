# Напишите функцию, показывающую, отсортирован ли переданный ей в качестве параметра список (по возрастанию или убыванию).  
# Функция должна возвращать True, если список отсортирован, и False в противном случае. В основной программе запросите у пользователя 
# последовательность чисел для списка, после чего выведите сообщение о том, является ли этот список отсортированным изначально.

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1)) or all(lst[i] >= lst[i+1] for i in range(len(lst) - 1))

numbers = list(map(int, input("Enter a sequence of numbers separated by spaces: ").split()))

if is_sorted(numbers):
    print("The list is sorted.")
else:
    print("The list is not sorted.")
