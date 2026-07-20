import csv

# Task 3: List comprehensions practice
# Read the contents of ../csv/employees.csv into a list of lists
with open('../csv/employees.csv', mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    employees_list = list(csv_reader)
    
# Creating list of full names, skipping first header row
employee_names = [f"{row[0]} {row[1]}" for row in employees_list[1:]]

# Print the results
print(employee_names)

print("_" * 20)

# creat a new list containing the letter 'e'
e_names = [name for name in employee_names if "e" in name.lower()]

# Print list
print("Names containing 'e':")
print(e_names)