# Task 1: Writing and Testing a Decorator
import logging
from functools import wraps

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    # Decorator
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Positional parameters
        pos_params = list(args) if args else "none"
        
        # Keyword parameters
        kw_params = kwargs if kwargs else "none"
        
        result = func(*args, **kwargs)
        
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {pos_params}")
        logger.log(logging.INFO, f"keyword parameters: {kw_params}")
        logger.log(logging.INFO, f"return: {result}")
        
        return result
    return wrapper

# Function with no parameters returning nothing
@logger_decorator
def no_params():
    print("Hello, World!")
    return None

# Positional argument functions returning True
@logger_decorator
def var_positional(*args):
    return True

# Functions with variable keyword arguments that return the logger decorator
@logger_decorator
def var_keyword(**kwargs):
    return logger_decorator

# Mainline
if __name__ == "__main__":
    no_params()
    var_positional(1, 2, 3, "apple")
    var_keyword(a=10, b=20, c="hello")
    
    print("Program finished. Check ./decorator.log")