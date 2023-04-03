# Напишите   программу которая   возвращает   список. Заранее подготовьте  список  предметов  и  оценок  учащихся.
# Когда вы  вводите имя учащегося, то должны отображаться оценки этого учащегося.

def get_student_grades(student_name):
    student_grades = {
        'Askhat': [90, 80, 70, 60],
        'Asel': [85, 75, 65, 55],
        'Marzhana': [95, 88, 77, 66],
        'Alexey': [80, 70, 60, 50]
    }
    
    if student_name in student_grades:
        return student_grades[student_name]
    else:
        return None

student_name = input("Enter the name of the student: ")
student_grades = get_student_grades(student_name)

if student_grades:
    print(f"Grades for {student_name}: {student_grades}")
else:
    print(f"No grades found for {student_name}")
