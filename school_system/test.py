from Student import Student
from Teacher import Teacher

s1 = Student("Ani", "20", 18)
t1 = Teacher("Babayan", "50", "IT")
school = [s1, t1]

for school in school:
    print(school.introduce())
