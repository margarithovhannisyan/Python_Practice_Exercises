"""
homework 5
● Initialize a Python project in PyCharm called Student Management System
● Create a script called Homework5.py
● Create a script that gets the full name, age, and average grade of a student for the current year and
average grade for the previous year.
● If the age of the student is less than 18, print the student’s name, age, and tell that he/she is a
Primary School student; otherwise, print that the student is a college student
● Print the average grade of the student for two years. If it is less than 50, tell that the student fails;
otherwise, tell that the student passes.
● Do a necessary check on the age.
● Print in a readable and nice format. """

ERROR_MESSAGE = "Provided value is not a valid"
full_name = input("Please provide student's full name")

age = input("Please provide student's age")
while not age.isdigit():
    print(ERROR_MESSAGE)
    age = input("Please provide student's age")
else:
    age = int(age)

current_average_grade = input("Please provide student's current year average grade")
while not current_average_grade.replace(".", "", 1).isdigit():
    print(ERROR_MESSAGE)
    current_average_grade = input("Please provide student's current year average grade")
else:
    current_average_grade = float(current_average_grade)

previous_average_grade = input("Please provide student's previous year average grade")
while not previous_average_grade.replace(".", "", 1).isdigit():
    print(ERROR_MESSAGE)
    previous_average_grade = input("Please provide student's previous year average grade")
else:
    previous_average_grade = float(previous_average_grade)

if age < 18:
    print(f"{full_name}, being {age} years old, is a Primary School student")
else:
    print(f"{full_name}, being {age} years old, is a College student")

average_grade = (current_average_grade + previous_average_grade) / 2
if average_grade < 50:
    print(f"As {full_name}'s average grade is {average_grade}: exams are failed")
else:
    print(f"As {full_name}'s average grade is {average_grade}: exams are passed")