# class_pupils = input('введите имена учеников\n')
# Полина, Антон, Аресний, Евгений, Алексей, Тимур
# assertion - утверждение
# TDD -> test driven development
class_pupils = 'Полина, Антон, Аресний, Евгений, Алексей, Тимур'
correct_result = ['Полина', 'Антон', 'Аресний', 'Евгений', 'Алексей', 'Тимур']
# print('учение класса:', class_pupils)
result = class_pupils.split(', ')

assert result == correct_result, 'алгоритм реализован неверно'
print(result)
