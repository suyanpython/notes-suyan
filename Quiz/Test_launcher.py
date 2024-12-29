import json
import string
import os
from pathlib import Path

# Set the path to your target directory
# path = Path(r"C:\Users\Administrateur\Downloads\LINUX\LINUX\Scripting-shell\TP\Quiz")
path = Path(__file__).resolve().parent

# List all files and directories in the specified path
files_and_dirs = os.listdir(path)

# Filter out directories, only keep files
files = [f for f in files_and_dirs if os.path.isfile(os.path.join(path, f))]
# print(files)


# Display the list of files with numbers
print("Please choose a file by typing a number (1 to 6):")
for i, file in enumerate(files[:6], start=1):  # Limit to 1 to 6 files
    print(f"{i}. {file}")

# Ask the user to select a file by number
while True:
    try:
        choice = int(input("Enter the number of your choice: "))
        if 1 <= choice <= min(len(files), 6):
            selected_file = files[choice - 1]
            print(f"You selected: {selected_file}")
            break
        else:
            print(f"Please enter a number between 1 and {min(len(files), 6)}.")
    except ValueError:
        print("Invalid input. Please enter a number.")


file_path = path / selected_file
# Load JSON data from file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)



# Initialize score
score = 0
total_questions = len(data['questions'])

# Go through each question
for i, question in enumerate(data['questions'], start=1):
    print(f"Question {i}: {question['question']}")
    print(f"1. {question['answer-1']}")
    print(f"2. {question['answer-2']}")
    print(f"3. {question['answer-3']}")
    print(f"4. {question['answer-4']}")
    
    # Get user answer
    user_answer = input("Your answer (1-4): ")

    # Check if the answer is correct
    if user_answer == question['good-answer']:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {question['good-answer']}.\n")

# Calculate final score
print(f"Your final score: {score}/{total_questions}")
