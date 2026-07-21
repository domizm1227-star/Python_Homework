#Task 2: Read a CSV File
import csv
import traceback
import custom_module

def read_employees():
    employees_data = {}
    rows = []
    
    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            
            for index, row in enumerate(reader):
                if index == 0:
                    # Create header
                    employees_data["fields"] = row
                else:
                    rows.append(row)
        employees_data["rows"] = rows
        
        return employees_data
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        
        for trace in trace_back:
            stack_trace.append(
                f"file : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )
            
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        
        return None
employees = read_employees()
print(employees)

# Task 3
# Giving function a parameter
def column_index(column_name):
    # Return index
    return employees["fields"].index(column_name)
# Calling function and storing the result in a global variable
employee_id_column = column_index("employee_id")
print(employee_id_column)

# Task 4
#Create function first_name
def first_name(row_number):
    # Find the column index for first_name
    first_name_col = column_index("first_name")
    # Get the row from employees["rows"]
    row = employees["rows"][row_number]
    # Return the value at that column index
    return row[first_name_col]

# Task 5 Find the Employee: a function in a function
def employee_find(employee_id):
    # Inner function to check if a row matches
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    #Use filter() to find all matching rows
    matches = list(filter(employee_match, employees["rows"]))
    # Return list of matches
    return matches

#Task 6 Find employee using lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

# Task 7 Sorting the rows by last_name using lambda
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]

# Task 8 Creating a dict for an employee
def employee_dict(row):
    employee = dict(zip(employees["fields"][1:], row[1:]))
    return employee
print(employee_dict(employees["rows"][0]))

# Task 9 Creating a dict of dicts for all employees
def all_employees_dict():
    all_employees = {}
    for row in employees["rows"]:
        emp_id = row[0]
        all_employees[emp_id] = employee_dict(row)
    return all_employees
print(all_employees_dict())

# Task 10 Using the OS Module
import os
def get_this_value():
    return os.getenv("THISVALUE")
print(get_this_value())

# Task 11 Creating personal custom_module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
print(custom_module.secret)

# Task 12 Reading minutes
def read_csv_to_dict(filename):
    data = {}
    rows = []
    try:
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            data["fields"] = next(reader)
            for row in reader:
                rows.append(tuple(row))
        data["rows"] = rows
    except Exception as e:
        print("Errow reading file:", e)
    return data

def read_minutes():
    minutes1 = read_csv_to_dict("../csv/minutes1.csv")
    minutes2 = read_csv_to_dict("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

# Task 13 Creating minutes_set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)
minutes_set = create_minutes_set()
print("set1", "set2")

# Task 14 Convert to datetime
from datetime import datetime
def create_minutes_list():
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), list(minutes_set)))
    return minutes_list
minutes_list = create_minutes_list()
print(minutes_list)

# Task 15 Writing out Sorted List
def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    converted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list))
    
    with open("./minutes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)
    return converted_list
minutes_sorted = write_sorted_list()
print(minutes_sorted)
