def my_decorator(func):
    def wrapper():
        print("Something will print before the function")
        func()
        print("Something will print after the function")
    return wrapper
@my_decorator
def say_hello():
    print("Hello")
say_hello()