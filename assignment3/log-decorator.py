import logging
from functools import wraps

# Task 1: Writing and Testing a Decorator
# Setting up the logger
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("./decorator.log", "a")
logger.addHandler(file_handler)

# Decorator
def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Call the original function
        result = func(*args, **kwargs)
        
        # Format positional and keyword parameteres
        positional = args if args else "none"
        keyword =kwargs if kwargs else "none"
        
        # Write info to the log file
        logger.info(
            f"function: {func.__name__}\n"
            f"positional parameters: {positional}\n"
            f"keyword parameters: {keyword}\n"
            f"return: {result}\n"
        )
        
        return result
    
    return wrapper

# Function with no parameters and no return value
@logger_decorator
def say_hello():
    print("Hello, World!")
    
# Function with a variable number of positional arguments
@logger_decorator
def positional_function(*args):
    return True

# Function with no positional arguments and variable keyword arguments
@logger_decorator
def keyword_function(**kwargs):
    return logger_decorator

# Mainline
if __name__ == "__main__":
    say_hello()
    
    positional_function("apple", "banana", "orange")
    
    keyword_function(name="John", age=25, city="Denver")