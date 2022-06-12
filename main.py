from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []  # Creating empty list
for questions in question_data:
    questions_text = questions["text"]
    questions_answer = questions["answer"]
    new_question = Question(questions_text, questions_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")