# range(n) -> 0, 1, 2, n-1, [0,n)
numbers = []
for num in range(10):
    numbers.append(num)
print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
last_num = numbers.pop()  # like cut in word
print(numbers)
print(last_num)
