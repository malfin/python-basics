import json


def parse_marks(f_name):
    result = []
    with open(f_name, 'r', encoding='utf-8') as f:
        for row in f.read().splitlines():
            last_name, first_name, patronymic, row_marks = row.split(maxsplit=3)
            patronymic = patronymic.strip(',')
            marks = []
            for mark in row_marks.split(','):
                marks.append(int(mark.strip()))
            avg_mark = sum(marks) / len(marks)
            result.append([last_name, first_name, patronymic, marks, avg_mark])
    return result


def parse_marks_as_dict(f_name):
    result = []
    with open(f_name, 'r', encoding='utf-8') as f:
        for row in f.read().splitlines():
            last_name, first_name, patronymic, row_marks = row.split(maxsplit=3)
            patronymic = patronymic.strip(',')
            marks = []
            for mark in row_marks.split(','):
                marks.append(int(mark.strip()))
            avg_mark = sum(marks) / len(marks)
            result.append(
                {
                    'last_name': last_name,
                    'first_name': first_name,
                    'patronymic': patronymic,
                    'marks': marks,
                    'avg_mark': avg_mark
                }
            )
            # result.append(
            #     {
            #         0: last_name,
            #         1: first_name,
            #         2: patronymic,
            #         3: marks,
            #         4: avg_mark
            #     }
            # )
    return result


def show_marks(parsed_marks, raw=True, sep=' '):
    for row in parsed_marks:
        if raw:
            print(row)
        else:
            print(sep.join(map(str, row)))


def show_students(parsed_marks):
    for row in parsed_marks:
        print(row[0], row[1], row[2])


def show_students_dict(parsed_marks_as_dict):
    for row in parsed_marks_as_dict:
        print(row['first_name'], row['last_name'], row['patronymic'])
        # print(row[0], row[1], row[2])



def save_marks(f_name, parsed_marks):
    head = ['last_name', 'first_name', 'patronymic', 'marks', 'avg_mark']
    with open(f_name, 'w', encoding='utf-8') as f:
        f.write(', '.join(head))
        f.write('\n')
        for row in parsed_marks:
            f.write(', '.join(map(str, row)))
            f.write('\n')


def save_marks_as_dict(f_name, parsed_marks_as_dict):
    with open(f_name, 'w', encoding='utf-8') as f:
        json.dump(parsed_marks_as_dict, f)