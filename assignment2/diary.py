#Task 1: Diary

import traceback
def main():
    try:
        with open("diary.txt", "a") as diary_file:
            prompt_text = "What happened today? "
        
        while True:
            user_input = input(prompt_text) 
            diary_file.write(user_input + "\n")
             # Checking for exit conditions
            if user_input == "done for now":
                break
            prompt_text = "What else? "
            
    except Exception as e:
    # Printing custom error alert
        print(f"An exception occured: {type(e).__name__}")
    
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = [
            f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            for trace in trace_back
        ]
        print(f"Stack trace: {stack_trace}")
    if __name__ == "__main__":
        main()