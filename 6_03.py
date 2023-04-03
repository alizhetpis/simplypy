# Общий объем расходов. Разработайте программу, которая подсчитает ваши расходы за каждый день недели. 
# Расходы по следующим категориям (транспортные расходы, обед, и т.д.) Суммы должны быть сохранены в списке. 
# Примените цикл, чтобы вычислить общий объем расходов за неделю и показать результат.

categories = ["Транспортные расходы", "Обед", "Продукты", "Развлечения", "Прочее"]
expenses = [[0] * len(categories) for _ in range(7)]
days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

# Вводим расходы по каждой категории за каждый день недели
for day in range(3):
    print(f"Введите расходы за {days_of_week[day]}")
    for i, category in enumerate(categories):
        expenses[day][i] = int(input(f"{category}: "))

# Считаем общий объем расходов за неделю
total_expenses = sum(sum(day) for day in expenses)

# Выводим суммы расходов по каждой категории и общий объем расходов за неделю
print("Расходы за неделю:")
for i, category in enumerate(categories):
    category_expenses = sum(day[i] for day in expenses)
    print(f"{category}: {category_expenses}")
print(f"Общий объем расходов за неделю: {total_expenses}")

