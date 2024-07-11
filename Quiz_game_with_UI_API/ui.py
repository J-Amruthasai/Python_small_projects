from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("QUIZZLER")
        self.window.config(padx=20, pady=20, bg="black")

        self.score_label = Label(text="Score: 0", fg="white", bg="black",font=("Arial",30,"bold"))
        self.score_label.grid(row=0, column=0 ,columnspan=3)

        self.canvas = Canvas(width=400, height=350, bg="white")
        self.question_text = self.canvas.create_text(200,175,width=280,text="Some Question Text",fill="black",font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_questions_left():
            self.score_label.config(text=f"Score: {self.quiz.scored}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz.\n\nFinal Score: {self.quiz.scored}",font=("Arial",20,"italic"))
            self.true_button.grid_remove()
            self.false_button.grid_remove()
            self.score_label.grid_remove()

            # self.true_button.config(state="disabled")
            # self.false_button.config(state="disabled")

    def true(self):
        self.correction(self.quiz.check_ans("True"))

    def false(self):
        is_right = self.quiz.check_ans("False")
        self.correction(is_right)

    def correction(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
