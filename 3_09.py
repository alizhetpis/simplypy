# Напишите программу, которая будет запрашивать у пользователя целочисленные  значения  и сохранять  их  ввиде  списка.  
# Индикатором окончания  ввода  значений  должен  служить  ноль.  Затем  программа должна  вывести  на  экран  
# все  введенные  пользователем  числа  (кроме нуля)   в порядке   возрастания – по   одному   значению   в строке. 
# Используйте для сортировки либо метод sort, либо функцию sorted.

numbers = []

while True:
    user_input = int(input("Enter number: "))
    if user_input == 0:
        break
    numbers.append(user_input)

sorted_numbers = sorted(numbers)

print("The sorted list of numbers:")
for number in sorted_numbers:
    print(number)
