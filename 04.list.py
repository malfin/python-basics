lesson_dates = [
    '19.05.15',
    '19.05.17',
    '19.05.18',
    '19.05.19',
    '19.05.22',
]
student_marks = [5, 4, 3, 2, 5]

# len(student_marks) -> 5
i = 0
while i < len(student_marks):
    # i == 0 < 5 -> True ?
    # i == 1 < 5 -> True ?
    # i -> 5, == 5 < 5 -> False ?
    print(lesson_dates[i], 'оценка', student_marks[i])
    i += 1  # i = 1
