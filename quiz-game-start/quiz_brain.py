class QuizBrain():
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answers = input(f"Q.{self.question_number}: {current_question.text}. "
                        f"(True/False): ").lower()
        self.check_answer(user_answers,current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score +=1
            print("You got it right")
        else:
            print("You got it wrong")
        print(f"Correct answer was {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")


