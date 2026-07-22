# Task 2: Decorator that takes an argument
def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

@type_converter(str)
def return_int():
    return "not a number"

@type_converter(int)
def return_string():
    return "not a number"

if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__)
    
    try:
        y = return_string()
        print("Shouldn't get here!")
    except ValueError:
        print("Can't convert that string to an intger!")
        