num_employees = int(input())  # количество сотрудников
vacation_schedule = {}  # словарь графика отпусков

# заполнение словаря графика отпусков
for i in range(num_employees):
    name, vacation_date = input().split()
    if name not in vacation_schedule:
        vacation_schedule[name] = []
    vacation_schedule[name].append(int(vacation_date))

requested_month = input()  # месяц, для которого нужно найти отпускающихся

employees_on_vacation = []  # список сотрудников, которые на отпуске в заданный месяц

# поиск сотрудников, у которых отпуск в заданный месяц
for name, vacation_dates in vacation_schedule.items():
    if int(requested_month) in vacation_dates:
        employees_on_vacation.append(name)

# вывод результатов
if employees_on_vacation:
    print(' '.join(employees_on_vacation))
else:
    print()
