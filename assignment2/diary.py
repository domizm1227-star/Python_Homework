#Task 1: Diary

import traceback
try:
    with open("diary.txt", "a") as diary_file:
        is_first_prompt = True
        
        while True:
            # Setting the prompt text dynamically depending on if it is the first prompt run
            prompt_text = "What happened today? " if is_first_prompt else "What else? "
            # Prompt user for input inside of loop
            user_input = input(prompt_text)
            diary_file.write(user_input + "\n")
             # Checking for exit conditions
            if user_input == "done for now":
                break

            is_first_prompt = False
            
except Exception as e:
    # Printing custom error alert
    print(f"An exception occured: {type(e).__name__}")
    
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
