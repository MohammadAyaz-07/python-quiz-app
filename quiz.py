import random

questions = [
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "b"
    },
    {
        "question": "What is the output of: print(type(10))?",
        "options": ["int", "<class 'int'>", "integer", "number"],
        "answer": "b"
    },
    {
        "question": "Which data type is used to store key-value pairs?",
        "options": ["list", "tuple", "dictionary", "set"],
        "answer": "c"
    },
    {
        "question": "What does len([1, 2, 3, 4]) return?",
        "options": ["3", "4", "5", "Error"],
        "answer": "b"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "<!-- -->"],
        "answer": "b"
    },
    {
        "question": "What is the output of: 2 ** 3?",
        "options": ["6", "8", "9", "Error"],
        "answer": "b"
    },
    {
        "question": "Which function is used to get user input in Python?",
        "options": ["scan()", "read()", "input()", "get()"],
        "answer": "c"
    },
    {
        "question": "Which of the following is an immutable data type?",
        "options": ["list", "dictionary", "set", "tuple"],
        "answer": "d"
    },
    {
        "question": "What does the break statement do in a loop?",
        "options": [
            "Skips current iteration",
            "Stops the loop completely",
            "Restarts the loop",
            "Pauses the loop"
        ],
        "answer": "b"
    },
    {
        "question": "Which keyword is used to handle exceptions?",
        "options": ["catch", "handle", "try", "error"],
        "answer": "c"
    }
]


def ask_question(question):
    print("\n" + question["question"])
    for idx, option in enumerate(question["options"]):
        print(f"{chr(97 + idx)}) {option}")

    user_answer = input("Enter option: ").strip().lower()

    if user_answer == question["answer"]:
        print("✅ Correct!")
        return True
    else:
        correct_option = question["options"][ord(question["answer"]) - 97]
        print(f"❌ Incorrect! Correct answer: {correct_option}")
        return False


def run_quiz(questions):
    score = 0
    random.shuffle(questions)

    for question in questions:
        if ask_question(question):
            score += 1

    print(f"\n🎯 Final Score: {score} / {len(questions)}")


def main():
    while True:
        print("\n=== QUIZ APP ===")
        print("1. Ask a random question")
        print("2. Run full quiz")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            ask_question(random.choice(questions))
        elif choice == "2":
            run_quiz(questions)
        elif choice == "3":
            print("Thanks for playing! 👋")
            break
        else:
            print("Please choose a valid option.")


if __name__ == "__main__":
    main()
