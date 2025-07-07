"""
homework 5
● Create a script that gets the full name, age, and average grade of a student for the current year and
average grade for the previous year.
● If the age of the student is less than 18, print the student’s name, age, and tell that he/she is a
Primary School student; otherwise, print that the student is a college student
● Print the average grade of the student for two years. If it is less than 50, tell that the student fails;
otherwise, tell that the student passes.
● Do a necessary check on the age.
● Print in a readable and nice format.

homework7
• Change the code to accept data for more than one student
• Add one more input, which asks about inputting a new student or stopping. If yes, continue inputting; if
no, stop inputting and print all students’ data.
• Add one more input that asks about the maximum number of students. And automatically stop inputting
students’ data when it reaches that number
"""

ERROR_MESSAGE = "Provided value is not a valid"
full_name_values = []
age_values = []
average_grade_values = []

number_of_students=input("Please provide the number of students")
while not number_of_students.isdigit():
    print(ERROR_MESSAGE)
    number_of_students=input("Please provide the number of students")
else:
    number_of_students=int(number_of_students)

for i in range(number_of_students):
    question =input("Do you want to provide a new student details? Yes/No")
    if question.lower()=="yes":
        full_name = input("Please provide student's full name")
        full_name_values.append(full_name)
        age = input("Please provide student's age")
        while not age.isdigit():
            print(ERROR_MESSAGE)
            age = input("Please provide student's age")
        else:
            age_values.append(int(age))

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

        average_grade = (current_average_grade + previous_average_grade) / 2
        average_grade_values.append(average_grade)
    elif question.lower() == "no":
        break
    else:
        print("Accepted values are Yes or No")
        question=input("Do you want to provide a new student details? Yes/No")

for i in range(len(full_name_values)):
    full_name = full_name_values[i]
    age = age_values[i]
    average_grade=average_grade_values[i]
    if age < 18:
        print(f"{full_name}, being {age} years old, is a Primary School student")
    else:
        print(f"{full_name}, being {age} years old, is a College student")

    if average_grade < 50:
        print(f"As {full_name}'s average grade is {average_grade}: exams are failed")
    else:
        print(f"As {full_name}'s average grade is {average_grade}: exams are passed")