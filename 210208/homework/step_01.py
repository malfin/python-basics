import random

file_name = "some_csv.csv"

lines = open(file_name).read().split(',')
myline = random.choice(lines)
print(myline)
