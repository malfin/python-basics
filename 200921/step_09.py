# class_pupils = input('введите имена учеников\n')

class_pupils = 'Полина,Антон, Аресний , Евгений, Алексей, Тимур'
correct_result = ['Полина', 'Антон', 'Аресний', 'Евгений', 'Алексей', 'Тимур']

_result = class_pupils.split(',')
result = []
for item in _result:
    # result.append(item.strip().lower().title())
    result.append(item.strip().title())

print(result)
assert result == correct_result, 'алгоритм реализован неверно'
