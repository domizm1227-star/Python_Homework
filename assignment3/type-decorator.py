# Task 2: Decorator that takes an argument
def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Calling function
            x = func(*args, **kwargs)
            # Convert and return result using the type specified
            return type_of_output(x)
        return wrapper
    return decorator
# Convert float/int result to a string
@type_converter(str)
def add_numbers(a, b):
    return a + b
#Convert a string result to an int
@type_converter (int)
def get_age_string():
    return "25"
#Convert int to a float
@type_converter(float)
def double_val(val):
    return val * 2

result1 = add_numbers(7, 9)
print(f"Result: {result1!r} | {type(result1)}")

result2 = get_age_string()
print(f"Result: {result2!r} | Type: {type(result2)}")

result3 = double_val(4)
print(f"")

def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

#return_int with type_converter passing str
@type_converter(str)
def return_int():
    return 5

result = return_int()
print(result)
print(type(result))

# Assuming type_converter is defined as follows:
def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator
# Decorating return_string with type_converter passing int
@type_converter(int)
def return_string():
    return "not a number"
try:
    y = return_string()
    print("shouldn't get here!")
except ValueError as e:
    print(f"Caught expected error: {e}")
    
    # Mainline
    y = return_int()
    print(type(y).__name__)
    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!") 