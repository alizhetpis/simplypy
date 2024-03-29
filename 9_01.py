# Функциональная функция - это функция, которая возвращает значение на основе входных данных. 
# Она не зависит от состояния программы и всегда возвращает одинаковый результат для одних и тех же входных данных. 
# Функциональная функция может быть использована в любом месте программы, где нужно получить результат ее выполнения.

# Нефункциональная функция - это функция, которая не возвращает значения, но выполняет какое-то действие, 
# например, выводит информацию на экран или изменяет состояние программы. 
# Нефункциональная функция не может быть использована в качестве параметра в другой функции или операторе, где требуется возвращаемое значение.

# Пример функциональной функции:
def calculate_salary(hours, rate):
    """
    Функция для вычисления заработной платы на основе количества часов работы и ставки за час
    """
    salary = hours * rate
    return salary

# Пример нефункциональной функции:
def print_employee_info(name, position, salary):
    """
    Функция для вывода информации о сотруднике на экран
    """
    print(f"Сотрудник {name} занимает должность {position} и получает зарплату {salary} тенге")
