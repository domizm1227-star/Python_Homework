import pandas as pd
import json
import numpy as np

# Task 1: Intro to Pandas-Creating and Manipulating DataFrames
# 1: Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data)
print("Task 1.1 DataFrame:")
print(task1_data_frame)

# 2: Add a new column
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]

print("\nTask 1.2 DataFrame with Salary:")
print(task1_with_salary)

# 3: Modify an existing column
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1

print("\nTask 1.3 Older DataFrame")
print(task1_older)

# 4: Saving the DataFrame as a CSV file
task1_older.to_csv('employees.csv', index=False)
print("\nTask 1.4: Saved task1_older to employees.csv successfully.")

# Task 2: Loading Data from CSV and JSON
# Read data from CSV file
task2_employees = pd.read_csv('employees.csv')
print("--- Task 2 CSV Data ---")
print(task2_employees)

# Step 2: Create JSON file with additional employees
add_data = [
    {'Name': 'Eve', 'Age': 28, 'City': 'Miami', 'Salary': 60000},
    {'Name': 'Frank', 'Age': 40, 'City': 'Seattle', 'Salary': 95000},
]

with open('additional_employees.json', 'w') as f:
    json.dump(add_data, f, indent=4)
    
# Loading the JSON file into a DataFrame
json_employees = pd.read_json('additional_employees.json')

print("\n--- JSON Data ---")
print(json_employees)

# Step 3: Combine DataFrames and reset index
more_employees = pd.concat(
    [task2_employees, json_employees], ignore_index=True
)
print("\n--- Combined Data ---")
print(more_employees)

# Task 3: Data Inspection using Head, Tail, and Info methods
# Step 1: Using the head() method
first_three = more_employees.head(3)
print("--- First Three Rows ---")
print(first_three)

# Step 2: Using the tail() method
last_two = more_employees.tail(2)
print("--- Last Two Rows ---")
print(last_two)

# Step 3: Getting the shape of the DataFrame
employee_shape = more_employees.shape
print("\n--- Shape of DataFrame ---")
print(employee_shape)

# Step 4: Using the info() method
print("\n--- Info Summary ---")
more_employees.info()

# Task 4: Data Cleaning
# Create DataFrame from dirty_data.csv
dirty_data = pd.read_csv('dirty_data.csv')
print("--- Dirty Data ---")
print(dirty_data)

# Create a copy in clean_data
clean_data = dirty_data.copy()

# Remove Duplicate rows
clean_data = clean_data.drop_duplicates()
print("\n--- After Removing Duplicates ---")
print(clean_data)

# Converting Age to numeric
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("\n---After Converting Age to Number ---")
print(clean_data)

# Converting Salary to numeric
clean_data['Salary'] = clean_data['Salary'].replace(
    ['unknown', 'n/a'], pd.NA
)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print("\n--- After converting Salary to Numeric ---")
print(clean_data)

# Fill in missing numeric values
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print("\n--- After Filling Missing Values ---")
print(clean_data)

# Converting Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(
    clean_data['Hire Date'], format='mixed', errors='coerce'
)
print("\n--- After Converting Hire Date to Datetime ---")
print(clean_data)

# Strip off extra whitespace and Standardize Name and Department
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()

print("\n--- Final Clean Data ---")
print(clean_data) 
