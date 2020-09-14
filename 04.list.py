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

lesson_dates_and_mark = [
    ['19.05.15', 5],
    ['19.05.17', 4],
    ['19.05.18', 3],
    ['19.05.19', 2],
    ['19.05.22', 5],
]

# for i, mark in enumerate(student_marks):
#     print(lesson_dates[i], 'оценка', mark)

for lesson_dates, mark in lesson_dates_and_mark:
    print(lesson_dates, 'оценка', mark)
