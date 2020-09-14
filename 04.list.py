lesson_dates = [
    '19.05.15',
    '19.05.17',
    '19.05.18',
    '19.05.19',
    '19.05.22',
]
student_marks = [5, 4, 3, 2, 5]

# i = 0
# while i < len(student_marks):
#     print(lesson_dates[i], 'оценка', student_marks[i])
#     i += 1  # i = 1
#
# for mark in student_marks: #mark
#     print('оценка', mark)
#
# user_full_name = ['Ivan', 'Ivanov']
# first_name = user_full_name[0]
# second_name = user_full_name[1]
#
# # first_name, second_name = ['Ivan', 'Ivanov']
# print(first_name, second_name)

for i, mark in enumerate(student_marks):
    print(lesson_dates[i], 'оценка', mark)
