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
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer: (A, B, C, D) ").upper()
        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong. The correct answer was:", question["answer"])
        print(question["explanation"])
        print()  # Add a blank line for better readability
    print(f"You got {score} out of {len(questions)} questions correct")


run_quiz(questions)
