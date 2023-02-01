# Information about the student
student_name = "Ali Zhetpis"
student_birthday = "11 March 2000"
student_major = "Computer Science"

# Using print() function to display student information
print("Student Name:", student_name)
print("Birthday:", student_birthday)
print("Major:", student_major)

# Taking input from the user
print('Course: ')
student_course = int(input())
print("Course:", student_course)

# Using conditional statements to display additional information
if student_course >= 3:
    print("Student is in the upper class")
elif student_course >= 1:
    print("Student is in the lower class")
else:
    print("Student is not enrolled")

# This is how Git works!
# New commit on Git