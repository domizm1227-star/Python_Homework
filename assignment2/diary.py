#Task 1: Diary

import traceback
try:
    with open("diary.txt", "q") as diary_file:
        first_prompt = True
        
        while True:
            if first_prompt:
                line = input("What happened today? ")
                first_prompt = False
            else:
                line = input("What else? ")
                
            diary_file.write(line + "\n")
            
            if line == "done for now:":
                break
            
except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
            
        
#Task 2: Read a CSV File
import csv
import traceback

def read_employees():
    employees_data = {}
    rows = []
    
    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            
            for index, row in enumerate(reader):
                if index == 0:
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