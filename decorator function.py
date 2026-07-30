def greet_decorator(func):
    def wrapper():
        print("before greetting")
        func()
        print("after greeting")
    return wrapper
@greet_decorator
def say_hello():
    print("hello")
say_hello()