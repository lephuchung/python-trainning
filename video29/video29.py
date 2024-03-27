from Quiz import Quiz

questions = [
    "Question 1: 1 + 1 = ? \nA. 2\nB. 3\nC. 1\n",
    "Question 1: 1 * 1 = ? \nA. 2\nB. 3\nC. 1\n",
    "Question 1: 1 / 1 = ? \nA. 2\nB. 3\nC. 1\n",
]

quizzes = [
    Quiz(questions[0], "A"),
    Quiz(questions[1], "C"),
    Quiz(questions[2], "C")
]


def run_quiz(quizes):
    score = 0
    for quiz in quizes:
        print(quiz.question)
        user_input = input("Enter your answer: ")
        if user_input.lower() == quiz.answers.lower():
            score += 1

    print(f"\nYour score is {score}/{len(quizes)}")


run_quiz(quizzes)
