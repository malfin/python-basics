student_marks = []
appraisal = [
    1,
    2,
    3,
    4,
    5
]
while True:
    mark = input('Введите оценку студента:\n')
    if mark != list(appraisal):
        student_marks.append(mark)
    else:
        break
print('Ввод завершен')
print(student_marks)
