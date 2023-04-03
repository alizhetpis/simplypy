# Функция, возвращающая список, кортеж, число или словарь:

def get_student_info(name, age, grade):
    """
    Функция для получения информации о студенте
    """
    student_tuple = (name, age, grade)
    student_list = [name, age, grade]
    student_dict = {"name": name, "age": age, "grade": grade}
    student_number = age + grade
    return student_list, student_tuple, student_number, student_dict
