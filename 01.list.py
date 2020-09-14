student_marks = []
while True:
    mark = input('Введите оценку студента:\t')
    if mark:
        student_marks.append(mark)
    else:
        break
print('Ввод завершен')
print(student_marks)
# ['5', '4', '3', '2']
#   0    1    2    3
i = 0
avg_mark = 0
while i < len(student_marks):
    # print(type(avg_mark), type(student_marks))
    # avg_mark = avg_mark + int(student_marks[i])
    avg_mark += int(student_marks[i])
    # i = i + 1
    i += 1
avg_mark /= len(student_marks)
print('Средний балл:', avg_mark)
