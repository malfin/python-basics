# Подсчёт кол-во строк (включая пустые строки)

def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result


csv_gen = csv_reader("some_csv.txt")
row_count = 0

for row in csv_gen:
    row_count += 1

print(f"Количество строк: {row_count}")
