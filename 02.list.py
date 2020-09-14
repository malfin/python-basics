# data read
# student_marks = []
# while True:
#     mark = input('Введите оценку студента:\n')
#     if mark:
#         student_marks.append(int(mark))
#     else:
#         break
# print('Ввод завершен')
# print(student_marks)

# mock_student_marks = ['5', '4', '3', '2', '5'] wrong mock
mock_student_marks = [5, 4, 3, 2, 5]  # correct mock
student_marks = mock_student_marks
# data processing
i = 0
avg_mark = 0
while i < len(student_marks):
    avg_mark += int(student_marks[i])
    i += 1
avg_mark /= len(student_marks)
print('Средний балл:', avg_mark)
