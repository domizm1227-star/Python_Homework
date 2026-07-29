# Task 1: Creating and manipulating dataframes
# 1.1.1 Create a DataFrame from dictionary
import pandas as pd

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
print()

