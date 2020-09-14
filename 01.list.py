import sys

# all is object! OOP:
#
# обекты (пользователь:
#       - атрибуты: св-ва (id, name, login, password)
#       - методы: действия (edit, delete, create, input_data)

# 'yan.ru' -> reference
# my_var = [12, '15', 95.32, 55, True]  # var -> referecnce
# print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))
#
# my_var = 12
# print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))
#
# my_var = 12.5
# print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))
#
# my_var = '12.5'
# print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))

student_marks = []

while True:
    mark = input('Введите оценку студента:\t')
    if mark:  # '' == False, 0 == False, [] == False
        student_marks.append(mark)
    else:
        break
print('Ввод завершен')
print(student_marks)
