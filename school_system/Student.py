from Person import Person


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.__grade = grade

    def set_grade(self, grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def introduce(self):
        return (
            f"Hello, I am student {self.get_name()} from {self.get_grade()} grade, "
            f"I am {self.get_age()} years old")
