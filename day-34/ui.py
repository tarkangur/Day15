import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(text="Score: 0", bg=THEME_COLOR, highlightthickness=0, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Question",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic")
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=true_img, highlightthickness=0, command=self.is_true)
        self.true_button.grid(row=2, column=0)

        false_img = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_img, highlightthickness=0, command=self.is_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_next = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_next)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the en of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def is_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
