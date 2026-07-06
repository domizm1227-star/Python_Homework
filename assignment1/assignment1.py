# Write your code here

# Task 1
from unittest import result


def hello():
    return "Hello!"

# Task 2
def greet(name):
    return f"Hello, {name}!"

# Task 3
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
                return "Unknown operation!"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
# Task 4
def data_type_conversion(value, type_name):
    try:
        match type_name:
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "int":
                return int(value)
            case _:
                return f"Unknown type {type_name}"
    except ValueError:
        return f"You can't convert {value} into a {type_name}."

# Task 5
def grade(*args):
    try:
        average = sum(args) / len(args)
        
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except Exception:
        return "Invalid data was provided."
    
# Task 6
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

# Task 7
def student_scores(mode, **kwargs):
    try:
        if mode == "best":
            best_student = None
            best_score = -1

            for name, score in kwargs.items():
                if score > best_score:
                    best_score = score
                    best_student = name
            return best_student
        elif mode == "mean":
            return sum(kwargs.values()) / len(kwargs)
        else:
            return "Invalid mode."

    except Exception:
        return "Invalid data was provided."

# Task 8
def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = text.split()
    result = []
    
    for i, word in enumerate(words):
        lower_word = word.lower()
        
        if i == 0 or i == len(words) - 1:
            result.append(lower_word.capitalize())
        elif lower_word not in little_words:
            result.append(lower_word.capitalize())
        else:
            result.append(lower_word)
    return " ".join(result)
# Task 9
def hangman(secret_word, guessed_word):
    result = ""
    for letter in secret_word:
        if letter in guessed_word:
            result += letter
        else:
            result += "_"
    return result
#Task 10
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result = []
    
    for word in words:
        # Start with a vowel
        if word[0] in vowels:
            result.append(word + "ay")
            continue
        # Start with "qu"
        index = 0
        while index < len(word) and word[index] not in vowels:
            if word[index:index+2] == "qu":
                index += 2
            else:
                index += 1
        result.append(word[index:] + word[:index] + "ay")
        continue
    
    return " ".join(result)
#print(hello())
#print(greet("Dominique"))
#print(calc(5, 7, "add"))
#print(calc(14, 36, "subtract"))
#print(calc(35, 84, "multiply"))
#print(calc(20, 75, "divide"))
#print(calc(30, 0, "modulo"))
#print(calc(0, 8, "int_divide"))
#print(calc("hello", "world", "multiply"))
#print(data_type_conversion("123", "int"))
#print(data_type_conversion("nonsense", "float"))
#print(data_type_conversion(5.7, "str"))
#print(grade(90, 95, 100, 100, 76, 84))
#print(grade(78, 60, 67, 64, 44, 100, 100))
#print(grade("oopsie", 78, 89, 100, 89, 97))
#print(repeat("Hi", 3))
#print(repeat("Dom", 2))
#print(student_scores("best", Sarah=88, Chris=95, Susan=72))
#print(student_scores("mean", Sarah=80, Chris=90))
#print(student_scores("mean", Sarah="oopsies"))
#print(titleize("the wizard of oz"))
#print(titleize("harry potter and the sorecerer's stone"))
#print(hangman("buffalo", "fba"))
#print(hangman("pancreas", "aes"))
#print(hangman("beehooves", "ohs"))
#print(pig_latin("duplex"))
#print(pig_latin("exposition"))
#print(pig_latin("interem"))
#print(pig_latin("Thank you and blow the flowers"))
#print(pig_latin("My name is Dominique"))
#print(pig_latin("quick"))
