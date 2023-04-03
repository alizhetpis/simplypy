# Напишите программу, которая, как и в предыдущем случае, будет запрашивать у пользователя целые числа и сохранять их в виде списка. 
# Индикатором окончания ввода значений также должен служить ноль. На этот раз необходимо вывести на экран введенные значения в порядке убывания.

numbers = []

while True:
    number = int(input("Enter number: "))
    if number == 0:
        break
    numbers.append(number)

numbers.sort(reverse=True)

for number in numbers:
    print(number)
