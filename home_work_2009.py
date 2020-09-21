# 1. Добавить к алгоритму вычислению среднего балла проверку,
# чтобы оценка была в диапазоне от 1 до 5.
#
# student_marks = []
# while True:
#     mark = input('Введите оценку студента:\n')
#     if mark:
#         student_marks.append(int(mark))
#         if int(mark) > 5:
#             print('Введите оценку от 1 до 5!')
#             student_marks.remove(int(mark))
#         elif int(mark) == 0:
#             print('Введите оценку от 1 до 5!')
#             student_marks.remove(int(mark))
#     else:
#         break
# print('Ввод завершен')
# avg_mark = 0
# for marks in student_marks:
#     avg_mark += marks
# avg_mark /= len(student_marks)
# if not student_marks:
#     print('Пусто)')
# else:
#     print('Оценки:', student_marks)
#     print('Средний балл:', avg_mark)

# 2. Вывести оценки студентов за конкретную дату
# (всё что есть, "Введите дату\n", после этого вывести оценку за эту дату)
# НЕ СДЕЛАЛ!
lesson_dates = [
    '19.05.15',
    '19.05.17',
    '19.05.18',
    '19.05.19',
    '19.05.22',
]
student_marks = [
    5,
    4,
    3,
    2,
    5
]
student_2_marks = [
    4,
    3,
    5,
    5,
    4
]

for lesson_dates, mark, mark_2 in zip(lesson_dates, student_marks, student_2_marks):
    print(lesson_dates, 'оценка', mark, mark_2)
date = input('Введите дату:\n')

date_index = lesson_dates.index(date)
print(date_index)
print('оценки студентов за ', lesson_dates[date_index], ':', student_marks[date_index], student_2_marks[date_index])
#
# say = 'Hello World!'
# print(say, len(say))
#
# say_2 = say.upper()
# print(say_2 * 3)
#
# say_3 = say.capitalize()
# print(say_3[2])
