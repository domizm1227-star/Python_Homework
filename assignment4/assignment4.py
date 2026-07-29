# Task 1: Creating and manipulating dataframes
# 1.1.1 Create a DataFrame from dictionary
import pandas as pd
from pathlib import Path
import json
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
# 1.1.2 Converting dictionary into dataframe
task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)

# 1.1.3 Saving as a csv file tab delimiter
task1_data_frame.to_csv('task1_data_frame', sep="\t", index=False)

# 1.1.4 Print new dataframe
print(task1_data_frame)

# 1.2.1 Adding a new column
# Make copy of task1_data_frame
task1_with_salary = task1_data_frame.copy()

# 1.2.2 Adding column Salary
task1_with_salary['Salary'] = [70000, 80000, 90000]

# 1.2.3 Print Salary
print(task1_with_salary)

# 1.3.1 Modifying an existing column
# Making a copy
task1_older = task1_with_salary.copy()

# 1.3.2 Increment Age by 1 by each entry
task1_older['Age'] = task1_older['Age'] + 1

# 1.3.4 Print
print(task1_older)

# 1.4.1 Saving the DataFrame as a CSV file
# Save to a file named employees.csv
task1_older.to_csv('employees.csv', index=False)

# Task 2: Loading Data from CSV and JSON
# 2.1.1 Read data from CSV file
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

# 2.2.1 Reading from a JSON file
additional_employees = [
{"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
{"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}]

# Adding new data into JSON file
with open("additional_employees.json","w") as file:
    json.dump(additional_employees, file)

# Loading the JSON file into a new DataFrame
json_employees = pd.read_json('additional_employees.json')

# 2.3.1 Combining DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)

# Task 3: Data Inspection using Head, Tail and Info methods
# 3.1 Using the head() method
first_three = more_employees.head(3)
print(first_three)

# 3.2 Using the tail() method
last_two = more_employees.tail(2)
print(last_two)

# 3.3 Getting the shape of the DataFrame
employee_shape = more_employees.shape
print(employee_shape)

# Task 4: Data Cleaning
# 4.1 Create DataFrame from dirty_data.csv and assign the dirty_data variable
dirty_data = pd.read_csv('dirty_data.csv')
print(dirty_data)

# Creating a copy of dirty_data
clean_data = dirty_data.copy()

# 4.2 Remove any duplicate rows
clean_data = clean_data.drop_duplicates()
print(clean_data)

# 4.3 Convert age to numeric handling missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print(clean_data)

# 4.4 Convert Salary to numeric and replace known placeholders with NaN
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a', 'N/A', 'Unknown'], np.nan)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print(clean_data)

# 4.5 Filling in any missing numeric values: Age with mean and Salary with median
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print(clean_data)

# 4.6 Convert Hire Date and datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print(clean_data)

# 4.7 Stripping extra whitespace and standardize Name and Department as uppercase
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.upper()
print(clean_data)