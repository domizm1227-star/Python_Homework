# Task 1: Writing and Testing a Decorator
import logging
from functools import wraps

#one-time logging setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    # Decorator logging function names, positional args, keyword args, and return value
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Logging function name
        logger.log(logging.INFO, f"function: {func.__name__}")
        
        # Positional parameters
        if args:
            logger.log(logging.INFO, f"positional parameters: {list(args)}")
        else:
            logger.log(logging.INFO, "positional parameters: none")

        # Keyword parameters
        if kwargs:
            logger.log(logging.INFO, f"keyword parameters: {kwargs}")
        else:
            logger.log(logging.INFO, "keyword parameters: none")
        
        # Calling original function
        result = func(*args, **kwargs)
        
        # log the return value 
        logger.log(logging.INFO, f"return value: {result!r}")
        
        return result

    return wrapper

# Function with no parameters, returns nothing
@logger_decorator
def greet():
    print("Hello, World!")

# Function with variable positional arguments, returns True
@logger_decorator
def check_args(*args):
    return True

# Function with variable keyword arguments, returns logger_decorator
@logger_decorator
def kw_return(**kwargs):
    return logger_decorator

#Mainline calls
if __name__ == "__main__":
    greet()
    check_args(1, 2, 3, "candy")
    kw_return (a=10, b=20, c="hello")
    
    print("Program finished. Check ./decorator.log for the logged output.")