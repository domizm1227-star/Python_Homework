# Task 2: Read CSV File

import csv
import sys
import os
import custom_module
from datetime import datetime

# Define function to read employees taking no arguments
def read_employees():
    # Setting up and initializing empty dictionary for employee_data and empty list rows
    employee_data = {}
    rows = []

# Open csv file
    try:
        with open("../csv/employees.csv", mode="r", newline="", encoding="utf-8") as file:
            # Initializing reader and track first_row
            reader = csv.reader(file)
            first_row = True
            
            # Loop through each row in reader
            for row in reader:
                if first_row:
                    employee_data["fields"] = row
                    first_row = False
                else:
                    rows.append(row)

            # Assign rows to employee_data
        employee_data["rows"] = rows
        # Catch exceptions
    except Exception as e:
        # Print error message
        print(f"Error reading CSV file: {e}")
        # exit with code 1
        sys.exit(1)

    return employee_data

# Storing result in global variable 'employees'
employees = read_employees()

if __name__ == "__main__":
    print(employees)
    
    
# Task 3: Find the column index
# Define function column_index that takes string 'column_name'
def column_index(column_name):
    # Fields list
    return employees["fields"].index(column_name)
# Store column index
employee_id_column = column_index("employee_id")

if __name__ == "__main__":
    print(employees)
    print(f"employee_id column index: {employee_id_column}")
    
    
# Task 4: Find the employee first name
# Define function first_name taking integer row numbers
def first_name(row_number):
    # Look up column index for first_name
    fn_index = column_index("first_name")
    # Access element at employees rows, row numbers and index
    # Return first name string
    return employees["rows"][row_number][fn_index]

if __name__ == "__main__":
    print(employees)
    print(f"employee_id column index: {employee_id_column}")
    if employees["rows"]:
        print(f"First name of employee at row 0: {first_name(0)}")
        
        
# Task 5: Find employee with a function in a function
# Define outer function employee_id
def employee_find(employee_id):
    # Define inner function employee_match
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))
    return matches

if __name__ == "__main__":
    print(employees)
    print(f"employee_id column index: {employee_id_column}")
    if employees["rows"]:
        print(f"First name at row 0: {first_name(0)}")
        

# Task 6: Find employee with a Lambda
# Define function employee_find_2
def employee_find_2(employee_id):
    matches = list(
        filter(
            # call using inline lambda
            lambda row: int(row[employee_id_column]) == employee_id,
            employees["rows"],
        )
    )
    return matches

if __name__ == "__main__":
    print(employees)
    print(f"employee_id column index: {employee_id_column}")
    if employees["rows"]:
        print(f"First name at row 0: {first_name(0)}")
        
# Task 7: Find employee by last name using a lambda function
# Define function sort_by_last_name taking no arguments
def sort_by_last_name():
    # Get column index for last_name
    ln_index = column_index("last_name")
    # Calling sort in-place
    employees["rows"].sort(key=lambda row: row[ln_index])
    return employees["rows"]
# execute in-place sort at module load
sort_by_last_name()

if __name__ == "__main__":
    print(employees)
    print(f"employee_id column index: {employee_id_column}")
    if employees["rows"]:
        print(f"First name at row 0: {first_name(0)}")
        
        
# Task 8: Create a dict for an employee
# Define function employee_dict taking a list row
def employee_dict(row):
    # Initializing emp_dict
    emp_dict = {}
    # Pairing employees fields with row
    for header, value in zip(employees["fields"], row):
        if header != "employee_id":
            # Each header value pair
            emp_dict[header] = value
    return emp_dict

if __name__ == "__main__":
    print(employees)
    print(f"employee_id column index: {employee_id_column}")
    if employees["rows"]:
        print(f"First name at row 0: {first_name(0)}")
        

# Task 9: A dict of all dicts for all employees
# Define function all_employees_dict taking no arguments
def all_employees_dict():
    # Initializing empty dictionary function
    all_employees = {}
    # Looping through each row in employees rows
    for row in employees["rows"]:
        # Extracting employee_id
        emp_id = row[employee_id_column]
        # Map ID keyto nested employee dictionary
        all_employees[emp_id] = employee_dict(row)
    return all_employees
# Store result in global variable
all_employees = all_employees_dict()
print("All Employees Dict:", all_employees)

if __name__ == "__main__":
    print(employees)
    print(f"employee_id column index: {employee_id_column}")
    if employees["rows"]:
        print(f"First name at row 0: {first_name(0)}")
        

# Task 10: Use the os module
# Define function get_this_value taking no arguments
def get_this_value():
    # Fetch value of environment variable
    return os.getenv("THISVALUE")

if __name__ == "__main__":
    print(employees)
    print(f"employee_id column index: {employee_id_column}")
    if employees["rows"]:
        print(f"First name at row 0: {first_name(0)}")
    print("All Employees Dict:", all_employees)
    print(f"THISVALUE: {get_this_value()}")
    
# Task 11: Creating your own module
# Define function set_that_secret taking string new_secret
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

# Update module secret value
set_that_secret("open sesame")

if __name__ == "__main__":
    print(employees)
    print(f"employee_id column index: {employee_id_column}")
    if employees["rows"]:
        print(f"First name at row 0: {first_name(0)}")
    print("All Employees Dict:", all_employees)
    print(f"THISVALUE: {get_this_value()}")
    set_that_secret("open sesame")
    print("Updated custom_module secret:", custom_module.secret)
    
    
# Task 12: Read minutes1.csv and minutes2.csv
# Define function read_csv_as_tuples
def read_csv_as_tuples(file_path):
    data = {}
    rows = []
    
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            first_row = True
            
            for row in reader:
                if first_row:
                    data["fields"] = row
                    first_row = False
                else:
                    rows.append(tuple(row))
                    
            data["rows"] = rows
            
    except Exception as e:
        print(f"Error reading CSV file {file_path}: {e}")
        sys.exit(1)
        
    return data

# Define function read_minutes_csv
def read_minutes():
    # Minutes1
    m1 = read_csv_as_tuples("../csv/minutes1.csv")
    # Minutes2
    m2 = read_csv_as_tuples("../csv/minutes2.csv")
    return m1, m2

# Store results in global variables
minutes1, minutes2 = read_minutes("../csv/minutes1.csv")

print("Minutes 1:", minutes1)
print("Minutes 2:", minutes2)

if __name__ == "__main__":
    print(employees)
    print(f"employee_id column index: {employee_id_column}")
    if employees["rows"]:
        print(f"First name at row 0: {first_name(0)}")
    print("All Employees Dict:", all_employees)
    print(f"THISVALUE: {get_this_value()}")
    print("Updated custom_module secret:", custom_module.secret)
    
    
# Task 13: Create minutes_set
minutes1, minutes2 = read_minutes("../csv/minutes1.csv")

# Define function create_minutes_set taking no arguments
def create_minutes_set():
    # Convert minutes1 to set1
    set1 = set(minutes1["rows"])
    # Convert minutes2 to set2
    set2 = set(minutes2["rows"])
    return set1.union(set2)

# Store result in global variable
minutes_set = create_minutes_set()

print("Minutes Set:", minutes_set)

if __name__ == "__main__":
    print(f"employee_id column index: {employee_id_column}")
    if employees["rows"]:
        print(f"First name at row 0: {first_name(0)}")
    print("All Employees Dict:", all_employees)
    print(f"THISVALUE: {get_this_value()}")
    print("Updated custom_module secret:", custom_module.secret)
    
    
# Task 14: Convery to datetime
# Define function create_minutes)list taking no arguments
def create_minutes_list():
    # minutes_set to list
    minutes_list_raw = list(minutes_set)
    # Apply map
    transformed_list = list(
        map(
            lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
            minutes_list_raw,
        )
    )
    return transformed_list

# Store in global variable
minutes_list = create_minutes_list()

print("Minutes List:", minutes_list)

if __name__ == "__main__":
    print(employees)
    print(f"employee_id column index: {employee_id_column}")
    if employees["rows"]:
        print(f"First name at row 0: {first_name(0)}")
    print("All Employees Dict:", all_employees)
    print(f"THISVALUE: {get_this_value()}")
    print("Updated custom_module secret:", custom_module.secret)
    
    
# Task 15: Write out Sorted List
# Define function write_sorted_list taking no arguments
def write_sorted_list():
    # Sort chronologically
    minutes_list.sort(key=lambda x: x[1])
    #Apply map
    converted_list = list(
        map(
            lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
            minutes_list,
        )
    )
    # Open in write mode
    try:
        with open("./minutes.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            writer.writerows(converted_list)
    except Exception as e:
        print(f"Error writing to ./minutes.csv: {e}")
        sys.exit(1)

    return converted_list
# Calling function to generate
sorted_minutes_list = write_sorted_list()

if __name__ == "__main__":
    print(employees)
    print(f"employee_id column index: {employee_id_column}")
    if employees["rows"]:
        print(f"First name at row 0: {first_name(0)}")
    print("All Employees Dict:", all_employees)
    print(f"THISVALUE: {get_this_value()}")
    print("Updated custom_module secret:", custom_module.secret)
    print("Minutes List (Datetimes):", minutes_list)
    print("Sorted Minutes List (Strings):", sorted_minutes_list)