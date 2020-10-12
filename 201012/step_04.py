# inheritance

class People:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = None
        self.address = None
        self.mail = None
        self.phone_number = None

    def about_me(self):
        print('привет, меня зовут', self.first_name, self.last_name, '!')
        # print('hello, my name is', self.first_name, self.last_name, '!')


class Student(People):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.id_student = None
        self.group_number = None

    def say_group(self):
        print('my group is', self.group_number)


class Teacher(People):
    def __init__(self, first_name, last_name, patronymic, speciality='учитель'):
        super().__init__(first_name, last_name)  # call parent init
        self.patronymic = patronymic
        self.speciality = speciality

    def say_speciality(self):
        print('моя специальность', self.speciality)

    def about_me(self):  # method override
        print('привет, я учитель, меня зовут', self.first_name, self.patronymic, self.last_name, '!')


class HeadTeacher(Teacher):
    def call_teachers(self):
        print('everybody, come here!')

    def about_me(self):
        print('привет, я завуч, меня зовут', self.first_name, self.patronymic, self.last_name, '!')


student_1 = Student('Иван', 'Иванов')
student_1.about_me()
student_1.say_group()

# student_2 = Student()
# student_2.say_hello()
# student_2.say_group()
#
teacher_1 = Teacher('Петр', 'Петров', 'Петрович', 'математик')
teacher_1.about_me()
# teacher_1.say_group()
teacher_1.say_speciality()
#
# # class hierarchy: People -> Teacher -> HeadTeacher
teacher_2 = HeadTeacher('Эрнест', 'Сидоров', 'Сергеевич')
teacher_2.about_me()
teacher_2.say_speciality()
teacher_2.call_teachers()