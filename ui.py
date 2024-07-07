THEME_COLOR = "#375362"
import tkinter
import quiz_brain
import question_model
class QuizInterface:
    def __init__(self, quiz_brain: quiz_brain.QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR)

        #Score at top right
        self.score_label = tkinter.Label(text="Score: " + str(self.quiz.score), font=("Arial",12),background=THEME_COLOR,foreground="white")
        self.score_label.grid(column=1, row=0,padx=20,pady=18)


        #Center canvas
        self.question_text_canvas = tkinter.Canvas(width=300,height=180)
        self.question_text_canvas.config(background="white", highlightthickness=0)
        self.question_text_canvas.grid(column=0,row=1,columnspan=2,padx=30,pady=18)
        self.question_text = self.question_text_canvas.create_text(150,90, text="Placeholder text", fill=THEME_COLOR, font=("Arial",18),width=280)
        
        

        #Correct answer option
        self.correct = tkinter.PhotoImage(file=".\\images\\true.png")
        self.correct_button = tkinter.Button(image=self.correct,command=self.button_function_check_correct)
        self.correct_button.config(background=THEME_COLOR,padx=20,pady=15,highlightthickness=0,borderwidth=0)
        self.correct_button.grid(column=0,row=2)

        #Wrong answer option
        self.wrong = tkinter.PhotoImage(file=".\\images\\false.png")
        self.wrong_button = tkinter.Button(image=self.wrong)
        self.wrong_button.config(background=THEME_COLOR,highlightthickness=0,borderwidth=0, command=self.button_function_check_false)
        self.wrong_button.grid(column=1,row=2,padx=20,pady=15)

        self.new_question()
        
        #Loop to keep the window open
        self.window.mainloop()

    
    def check_if_correct(self, answer_to_check):
        if self.quiz.still_has_questions() is True:
            print("This code is running!!!")
            if answer_to_check is True:
                self.background_correct()
                self.window.after(1000, self.background_normal)
                self.quiz.update_score(True)
            else:
                self.background_wrong()
                self.window.after(1000,self.background_normal)
                self.quiz.update_score(False)

            self.window.after(1000,self.new_question)
        
        else:
            print("There is no more questions.")
        
        self.update_score_ui()
        
        
    def button_function_check_correct(self):
        answer = self.quiz.check_answer("true")
        self.check_if_correct(answer)
    
    def button_function_check_false(self):
        answer = self.quiz.check_answer("false")
        self.check_if_correct(answer)

    def new_question(self):
        self.question_text_canvas.itemconfig(self.question_text, text=self.quiz.next_question())

    def update_score_ui(self):
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")

    def background_normal(self):
        self.question_text_canvas.config(background="white")

    def background_correct(self):
        self.question_text_canvas.config(background="green")
    
    def background_wrong(self):
        self.question_text_canvas.config(background="red")
