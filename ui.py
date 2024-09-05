from tkinter import *

THEME_COLOR = "#375362"


class QuizInterFace:
    def __init__(self, quiz):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz APP")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_display = Label(self.window, text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 20))

        self.canvas = Canvas(self.window, bg="white", highlightthickness=0, width=600, height=500)
        self.text_question = self.canvas.create_text(300, 250, text="Question is here", width=400,
                                                     font=("Arial", 28, "italic"))

        true = PhotoImage(file="./images/true.png")
        false = PhotoImage(file="./images/false.png")

        self.button_true = Button(self.window, image=true, highlightthickness=0, command=lambda: self.check("False"))
        self.button_false = Button(self.window, image=false, highlightthickness=0, command=lambda: self.check("True"))

        self.button_true.grid(row=2, column=0, padx=20, pady=20)
        self.button_false.grid(row=2, column=1, padx=20, pady=20)
        self.score_display.grid(row=0, column=1, padx=20, pady=20)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.display_question()
        self.window.mainloop()

    def display_question(self):
        self.canvas.itemconfig(self.text_question, text=self.quiz.next_question())

    def check(self, answer):
        user_answer = answer
        if self.quiz.check_answer(user_answer):
            self.canvas.config(bg="#4CAF50")
            self.window.after(200, lambda: self.canvas.config(bg='white'))
        else:
            self.canvas.config(bg="#F44336")
            self.window.after(200, lambda: self.canvas.config(bg='white'))
        self.score_display.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            self.display_question()
        else:
            self.button_false.config(command=...)
            self.button_true.config(command=...)
            self.canvas.itemconfig(self.text_question, text=f"Your final score: {self.quiz.score}")
            self.score_display.config(text="")
