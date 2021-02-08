def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


a = range(5)
print(list(a))
