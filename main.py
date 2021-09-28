from data import questions
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in questions:
    question_bank.append(
        Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)

while(quiz.still_has_questions()):
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

input("\nPress ENTER to exit")
