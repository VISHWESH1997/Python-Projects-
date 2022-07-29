from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Ariel"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.can = self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(125, 150, font=(FONT_NAME, 20, "italic"),
                                                     text="data", fill=THEME_COLOR, width=250)
        # row = 0, 1, 2; column = 0, 1
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        tick = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=tick, highlightthickness=0, bg=THEME_COLOR, relief="flat",
                                   command=self.true_answer)
        self.right_button.grid(row=2, column=0)
        cross = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=cross, highlightthickness=0, bg=THEME_COLOR, relief="flat",
                                   command=self.wrong_answer)
        self.wrong_button.grid(row=2, column=1)

        self.score = 0
        self.score_label = Label(text=f"Score:{self.score}", fg="white", highlightthickness=0, bg=THEME_COLOR,
                                 font=(FONT_NAME, 12))
        self.score_label.grid(row=0, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of quiz!!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_answer(self):
        # is_right = self.quiz.check_answer("True")
        self.feedback(self.quiz.check_answer("True"))
        # both above and below calling of func is right
        # self.score += 1
        # self.score_label.config(text=f"Score:{self.score}")
        # self.next_question()

    def wrong_answer(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)
        # self.score_label.config(text=f"Score:{self.score}")
        # self.next_question()

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)
