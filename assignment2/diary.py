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
        print(f"An exception occured.")
        print(type(e).__name__)

if __name__ == "__main__":
    main()