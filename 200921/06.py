student_marks = []
while True:
    mark = input('введите оценку студента\n')
    if not mark:
        break
    if len(mark) != 1:
        print('Вы ввели не один символ!')
        continue
    # if not 48 <= ord(mark) <= 57:
    #     print('вы ввели не число!')
    #     continue
    if mark.isdigit():  # - проверяет от 0 до 9
        mark = int(mark)
        if 1 <= mark <= 5:
            student_marks.append(mark)
        elif mark > 5:
            print('Оценка больше 5!')
        elif mark < 1:
            print('Оценка меньше 1')
    else:
        print('Ошибка:', mark)
    # try:
    #     mark = int(mark)
    #     if 1 <= mark <= 5:
    #         student_marks.append(mark)
    #     elif mark > 5:
    #         print('Оценка больше 5!')
    #     elif mark < 1:
    #         print('Оценка меньше 1')
    # except Exception as e:  # ловит все ошибки
    #     print('Была допущена ошибка:', e)
print('ввод завершен', student_marks)
