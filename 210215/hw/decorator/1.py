def my_decorator(func):
    def wrapper():
        print("Что-то происходит до вызова функции.")
        func()
        print("Что-то происходит после вызова функции.")

    return wrapper


def say_whee():
    print("УРА!")


say_whee = my_decorator(say_whee)
