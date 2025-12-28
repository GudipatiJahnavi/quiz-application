questions = [
    {
        "question": "What is the output of print(2 + 3 * 4)?",
        "options": ["A. 20", "B. 14", "C. 24", "D. 10"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["A. List", "B. Set", "C. Dictionary", "D. Tuple"],
        "answer": "D"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /* */", "C. #", "D. <!-- -->"],
        "answer": "C"
    },
    {
        "question": "What does size() function return?",
        "options": ["A. Value", "B. Type", "C. Length", "D. Index"],
        "answer": "C"
    }
]

score = 0

for q in questions:
    print("\length" + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        score += 1

print("\nQuiz Completed!")
print("Your Score:", score, "/", len(questions))