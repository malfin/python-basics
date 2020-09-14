# student_marks = []
# while True:
#     mark = input('Введите оценку студента:\t')
#     if mark:
#         student_marks.append(mark)
#     else:
#         break
# print('Ввод завершен')
# print(student_marks)

mock_student_marks = ['5', '4', '3', '2', '5']
student_marks = mock_student_marks
i = 0
avg_mark = 0
while i < len(student_marks):
    avg_mark += int(student_marks[i])
    i += 1
avg_mark /= len(student_marks)
print('Средний балл:', avg_mark)
