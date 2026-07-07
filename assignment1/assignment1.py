# Write your code here.

# Task 1
def hello():
    return "Hello!"

# Task 2
def greet(name):
    return f"Hello, {name}!"

#Task 3
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
                raise ValueError("Invalid operation!")
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
#Task 4
def data_type_conversion(value, type_name): 
    try:
        if type_name == "float":
            return float(value)
        elif type_name == "int":
            return int(value)
        elif type_name == "str":
            return str(value)
        else:
            return None
    except ValueError:
        return f"You can't convert {value} into a {type_name}."
#Task 5
def grade(*args):
    try:
        if not args:
            return "Invalid data was provided."
        
        numbers = [float(x) for x in args]
        avg = sum(numbers) / len(numbers)
        
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
        
    except Exception:
        return "Invalid data was provided."
    
#Task 6
def repeat(string, count):
    result =""
    for _ in range(count):
        result += string
    return result

#Task 7
def student_scores(mode, **kwargs):
    if mode == "best":
        return max(kwargs, key=kwargs.get)
    elif mode == "mean":
        return sum(kwargs.values()) / len(kwargs)
    else:
        return "Invalid Mode!"
    
#Task 8
def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = text.split()
    result = []
    
    for i, word in enumerate(words):
        if i == 0 or i == len(words) -1:
            result.append(word.capitalize())
        elif word.lower() not in little_words:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
            
    return " ".join(result)

#Task 9
def hangman(secret_word, guessed_word):
    guessed_word = guessed_word.lower()
    result = []
    
    for ch in secret_word.lower():
        if ch == " ":
            result.append(" ")
        elif ch in guessed_word:
            result.append(ch)
        else:
            result.append("_") 
    return "".join(result)

#Task 10
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result = []

    for word in words:
        if not word:
            continue
        w = word.lower()

        if w[0] in vowels:
            result.append(w + "ay")

        elif w.startswith("qu"):
            result.append(w[2:] + "quay")

        else:
            # Find the first vowel
            i = 0
            while i < len(w) and w[i] not in vowels:
                i += 1

            consonants = w[:i]
            rest = w[i:]

            # Special handling for "qu" that appears after consonants
            if rest.startswith("qu"):
                result.append(rest[2:] + consonants + "quay")
            else:
                result.append(rest + consonants + "ay")

    return " ".join(result)

#print(hello())

#print(greet("Dominique"))

#print(calc(10, 7, "add"))
#print(calc(20, 7, "subtract"))
#print(calc(3, 8, "multiply"))
#print(calc(6, 8, "divide"))
#print(calc(15, 7, "modulo"))
#print(calc(7, 9, "int_divide"))
#print(calc(2, 0, "power"))
#print(calc(10, 9))

#print(data_type_conversion("banana", "int"))
#print(data_type_conversion(9.34, "int"))
#print(data_type_conversion(47, "str"))
#print(data_type_conversion("hello", "float"))

#print(grade(89, 98, 74, 100, 76))
#print(grade(76, 98, 99, 100, 97, 88))
#print(grade(100, 100, 100, 100, 100))
#print(grade("d", 90, "g", 100))

#print(repeat("hello", 3))
#print(repeat("sign", 5))
#print(repeat("testing", 2))

#print(student_scores("best", Dominique=89, Adam=98, Amber=74, Brandon=100, Kiara=90))
#print(student_scores("mean", Dominique=89, Adam=98, Amber=74, Brandon=100, Kiara=90))
#print(student_scores("best", Falicia=90, Betty=90))

#print(titleize("harry potter and the sorcerer's stone"))
#print(titleize("the cat in the hat"))
#print(titleize("barney"))

#print(hangman("hangman", "gma"))
#print(hangman("what is my name", "imn"))
#print(hangman("this is awesome", "isn"))

#print(pig_latin("duplex"))
#print(pig_latin("sphinx"))
#print(pig_latin("Dominique"))
#print(pig_latin("Adam"))
#print(pig_latin("Brandon"))
#print(pig_latin("Amber"))
#print(pig_latin("Kiara"))
#print(pig_latin("Dogs are so messy"))
#print(pig_latin("The baseball game ended quickly in the second half of the first quarter"))
#print(pig_latin("square"))