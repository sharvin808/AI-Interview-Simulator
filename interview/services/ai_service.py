import random

# Question database
QUESTIONS = {
    "Python Developer": [
        "What is Python and why is it used?",
        "Explain list vs tuple in Python.",
        "What are decorators in Python?",
        "Explain OOP concepts in Python.",
        "What is a Python virtual environment?"
    ],
    "Java Developer": [
        "What is JVM?",
        "Explain OOP concepts in Java.",
        "Difference between interface and abstract class.",
        "What is multithreading?",
        "Explain exception handling in Java."
    ],
    "web": [
        "What is HTML, CSS, and JavaScript?",
        "Difference between frontend and backend.",
        "What is REST API?",
        "Explain how HTTP works.",
        "What is responsive design?"
    ],
    "HR": [
        "Tell me about yourself.",
        "Why should we hire you?",
        "What are your strengths and weaknesses?",
        "Where do you see yourself in 5 years?",
        "Describe a challenge you faced."
    ]
}

def generate_question(role):
    #role = role.lower()

    if role in QUESTIONS:
        return random.choice(QUESTIONS[role])

    # Default fallback
    return "Tell me about yourself."