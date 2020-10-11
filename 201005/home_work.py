# Подумать, какие атрибуты вы бы задали для:
#   - студент (Student)
#   - учитель
#   - учебная группа
#   - колледж
#   - экзамен
#   - ученик на экзамене
#   - автомобиль

class Student:
    def __init__(self):
        self.id_student = None
        self.couples = None
        self.mark = None
        self.home_work = None
        self.teacher = None
        self.number_phone = None


class Teacher:
    def __init__(self):
        self.id_students = None
        self.couples = None
        self.mark_students = None
        self.missing = None
        self.home_work_students = None


class StudyGroup:
    def __init__(self):
        self.id_students = None
        self.room = None
        self.teacher = None
        self.number_phone = None


class College:
    def __init__(self):
        self.Str = None
        self.room = None
        self.teachers = None
        self.students = None


class Exam:
    def __init__(self):
        self.student = None
        self.mark = None
        self.teacher = None
        self.questions = None


class StudentExam:
    def __init__(self):
        self.student = None
        self.mark = None
        self.teacher = None
        self.questions = None
        self.ticket = None


class Car:
    def __init__(self):
        self.engine = None
        self.color = None
        self.brand = None
        self.mark = None
        self.number = None
        self.owner = None
        self.OSAGO = None
