# inheritance

class People:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = None
        self.address = None
        self.mail = None
        self.phone_number = None


# for Student parent class People => call .__init__() for parent => super() - parent method call
class Student(People):
    def __init__(self):
        super().__init__()  # creates parent attributes
        self.id_student = None
        self.group_number = None


# for Teacher parent class People => call .__init__() for parent
class Teacher(People):
    def __init__(self):
        super().__init__()
        self.patronymic = None
        self.group_curator = None