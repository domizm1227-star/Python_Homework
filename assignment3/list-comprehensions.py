import csv

# Task 3: List Comprehensions Practice

# Read employees.csv into a list of lists
with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)
    employees = list(reader)
    
# Create a list of employee names, skip the header
names = [employee[0] + " " + employee[1] for employee in employees[1:]]
print(names)

# Create a list containing only names with the letter "e"
names_with_e = [name for name in names if "e" in name]

print(names_with_e)