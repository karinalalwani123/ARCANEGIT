import random

questions = [
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Mercury", "B) Venus", "C) Jupiter", "D) Saturn"],
        "correct_answer": "C"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A) William Shakespeare", "B) Jane Austen", "C) Charles Dickens", "D) Mark Twain"],
        "correct_answer": "A"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"],
        "correct_answer": "B"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["A) Tokyo", "B) Beijing", "C) Seoul", "D) Bangkok"],
        "correct_answer": "A"
    }
]

random.shuffle(questions)

score = 0
question_number = 1  # Start questions from 1

def display_question(question_data, question_number):
    print("\nQuestion " + str(question_number) + ": " + question_data["question"])
    for option in question_data["options"]:
        print(option)
    user_answer = input("Enter the letter of your answer: ").strip().upper()

    if user_answer == question_data["correct_answer"]:
        print("Correct! 🎉")
        return True
    else:
        print("Incorrect. 😞 The correct answer is " + question_data["correct_answer"])
        return False

for question in questions:
    if display_question(question, question_number):
        score += 1
    question_number += 1

print("\nQuiz completed!")
print("Your score: " + str(score) + "/" + str(len(questions)))