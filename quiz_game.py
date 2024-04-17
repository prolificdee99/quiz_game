# Define a list of dictionaries, each containing a quiz question, options, correct answer, and explanation
questions = [
    {
        "prompt": " Who developed Python Programming Language?",
        "options": ["A.Wick van Rossum", "B.Rasmus Lerdorf", "C.Guido van Rossum", "D.Niene Stom"],
        "answer": "C",
        "explanation": "Guido van Rossum developed Python. He started working on Python in the late 1980s."
    },
    {
        "prompt": "Which type of Programming does Python support?",
        "options": ["A.object-oriented programming", "B.structured programming", "C.functional programming", "D.all of the mentioned"],
        "answer": "D",
        "explanation": "Python supports object-oriented, structured, and functional programming paradigms, making it versatile."
    },
    {
        "prompt": "Is Python case sensitive when dealing with identifiers?",
        "options": ["A.No", "B.Yes", "C.Machine dependent", "D.None of the answers"],
        "answer": "B",
        "explanation": "Yes, Python is case sensitive when dealing with identifiers. For example, 'my_variable' and 'My_Variable' are treated as different variables."
    },
    {
        "prompt": "Which of the following is the correct extension of the Python file?",
        "options": ["A. .python", "B. .pl", "C. .py", "D. .p"],
        "answer": "C",
        "explanation": "The correct extension for a Python file is '.py'. This is the standard convention for Python source code files."
    },
    {
        "prompt": "Which keyword is used for function in Python language?",
        "options": ["A.Function", "B.def ", "C.Fun", "D.Define "],
        "answer": "B",
        "explanation": "The 'def' keyword is used to define functions in Python. It is followed by the function name and parameters."
    }
]


def run_quiz(questions):
    # Initialize the score counter
    score = 0

    # Iterate through each question in the list
    for question in questions:
        # Print the question prompt
        print(question["prompt"])

        # Print each option for the question
        for option in question["options"]:
            print(option)

        # Get user's answer and convert to uppercase
        answer = input("Enter your answer: (A, B, C, D) : ").upper()

        # Check if the answer is correct
        if answer == question["answer"]:
            # Print feedback for correct answer
            print("Correct!")
            # Increment the score if answer is correct
            score += 1
        else:
            # Print feedback for incorrect answer
            print("Wrong. The correct answer was:", question["answer"])

        # Print the explanation for the question
        print(question["explanation"])

        # Add a blank line for better readability between questions
        print()

    # Print the final score
    print(f"You got {score} out of {len(questions)} questions correct")


# Call the function to run the quiz
run_quiz(questions)
