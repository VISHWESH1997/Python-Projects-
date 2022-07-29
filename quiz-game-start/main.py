from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]
for data in question_data:
    new_question = Question(data["text"], data["answer"])
    question_bank.append(new_question)

new_quiz = QuizBrain(question_bank)
while new_quiz.still_has_questions():
    new_quiz.next_question()

print(f"You have completed the quiz the final score was {new_quiz.score} / {new_quiz.question_number}")
