# Write your code here.

# Task 1: Hello
print("A1: Hello!")

# Task 2: Greet with a Formatted String
name = "Dominique"
print("A2: Hello", (name))

# Task 3: Calculator
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return f"Invalid operation: '{operation}'"
            
    except ZeroDivisionError:
        return "You can't divide by 0!"
    
    except TypeError:
        return "You can't perform that operation with those values!"


result = calc(3, 6, "add")
print("A3:", result)

result = calc(9, 0, "modulo")
print("A3:", result)

result = calc("y", "u", "subtract")
print(result)

# Task 4: Data Type Conversion
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "int":
                return int(value)
            case _:
                return f"You can't convert {value} into a {data_type}."
        
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {data_type}."
    
print("A4:", data_type_conversion("432.21", "float"))

# Task 5: Using Greading system(*args)
def grade(*args):
    try:
        if not args:
            return "Invalid data was provided."
        
        avg = sum(args) / len(args)
        
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
        
    except TypeError:
        return "Invalid data was provided."
    
print("A5:", grade(90, 95, 10))
print("A5:", grade(80, 85, 88))
print("A5:", grade(50, 60, 55))   
print("A5:", grade("nonsense", 90))

# Task 6: Use a For Loop with a Range
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

print("A6:", repeat("hello", 3))
print("A6:", repeat("a", 5))
print("A6:", repeat("xyz", 3))

# Task 7: Student Scores Using **kwargs
def student_scores(option, **kwargs):
    if option == "best":
        best_student = None
        highest_score = float("-inf")
        
        for student, score in kwargs.items():
            if score > highest_score:
                highest_score = score
                best_student = student
                
        return best_student
    
    elif option == "mean":
        scores = kwargs.values()
        return sum(scores) / len(scores)
    
print("A7:", student_scores("best", Amber=92, Brandon=85, Kiara=98))
print("A7:", student_scores("mean", Amber=90, Brandon=80, Kiara=100))

# Task 7: Titleize, with String and List Operations

def titleize(text):
    words = text.split()
    if not words:
        return ""
    
    little_words =["a", "on", "an", "the", "of", "and", "is", "in"]
    result = []
    
    last_index = len(words) - 1
    
    for i, word in enumerate(words):
        lower_word = word.lower()
        
        if i == 0 or i == last_index:
            result.append(lower_word.capitalize())
        elif lower_word in little_words:
            result.append(lower_word)
        else:
            result.append(lower_word.capitalize())
            
    return " ".join(result)

print("A8:", titleize("home alone 1, 2, 3"))
print("A8:", titleize("miracle on 34th street"))
print("A8:", titleize("alfred hitchcock the birds"))

# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

print("A9:", hangman("alphabet", "ab"))
print("A9:", hangman("python", "o"))
print("A9:", hangman("hello", "helo"))
print("A9:", hangman("secret", "xyz"))

# Task 10: Pig Latin, Another String Manipulation Exercise
def convert_word(word):
    vowels = "aeiou"
    
    # Rule 1: Starts with a vowel, 'ay' is put at the end
    if word[0] in vowels:
        return word + "ay"
    
    # Rule 3: Special case 'qu' at the beginning
    if word.startswith("qu"):
        return word[2:] + "quay"
    
    # Rules 2 & 3: Starts with one or more consenants
    i = 0
    while i < len(word) and word[i] not in vowels:
        if word[i:].startswith("qu"):
            i += 2
            break
        i += 1
        
    return word[i:] + word[:i] + "ay"

def pig_latin(text):
    words = text.split()
    pig_words = [convert_word(word) for word in words]
    return " ".join(pig_words)

print("A10:", pig_latin("nebula"))
print("A10:", pig_latin("midnight whisper"))
print("A10:", pig_latin("pineapple"))
print("A10:", pig_latin("quantum leap"))
print("A10:", pig_latin("velvet"))
print("A10:", pig_latin("the quiet mouse ran quick"))