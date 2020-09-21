a = 'всем привет'
# print(dir(a), '\n', type(a))
print(a.isdigit())
b = '15.7'
print(b.isdigit())

c = '157'
print(c.isdigit())

d = '15e6'
print(d.isdigit())

r = '15e6'
print(r.isdigit())

avg_mark = input('введите средний балл студента:\n')
# if avg_mark.isdigit():
#     avg_mark = float(avg_mark)
#     print('ввод корректен', type(avg_mark))
try:
    avg_mark = float(avg_mark)
    print('ввод корректен', type(avg_mark))
except ValueError as e:
    print('некоррентное значение', avg_mark, e)