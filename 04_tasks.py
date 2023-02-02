# 1 Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно. 
A = int(input("Enter A: "))
B = int(input("Enter B: "))

for i in range(A, B + 1):
    print(i)

# 2 Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, 
# если A < B, или в порядке убывания в противном случае.
def print_range(A, B):
    if A <= B:
        for i in range(A, B + 1):
            print(i)
    else:
        for i in range(A, B - 1, -1):
            print(i)

A = int(input("Enter A: "))
B = int(input("Enter B: "))
print_range(A, B)

# 3 Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, в порядке убывания. 
# В этой задаче можно обойтись без инструкции if.
def odd_numbers(A, B):
    for i in range(A - (A + 1) % 2, B - B % 2, -2):
        print(i)

A = int(input("Enter A: "))
B = int(input("Enter B: "))
odd_numbers(A, B)

# 4 Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек. 
# Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). Программа должна вывести номер потерянной карточки. 
# Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя. 

n = int(input("Enter N: "))
sum_of_numbers = n * (n + 1) // 2
for i in range(n - 1):
    sum_of_numbers -= int(input())
print("Lost card: ", sum_of_numbers)