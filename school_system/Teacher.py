from Person import Person


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.__subject = subject

    def set_subject(self, subject):
        self.__subject = subject

    def get_subject(self):
        return self.__subject

    def introduce(self):
        return (
            f"Hello, I am teacher {self.get_name()} teaching {self.get_subject()} subject, "
                f"I am {self.get_age()} years old")
