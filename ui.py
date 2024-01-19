from tkinter import *
from tkinter import messagebox
from config import *
from quiz_brain import QuizBrain
class QuizInterface():
    '''class QuizInterface to create the user interface for quiz app,arguments-->None'''
    
    def __init__(self,quiz_brain: QuizBrain):  # quiz_brain argument is of datatype QuizBrain data type
        # todo: assign quiz_bran object to quiz_deck QuizInterface attribute
        self.quiz_deck = quiz_brain
        # TODO: create a window base layout widget with pad of 20 on x and 20 on y with bg = "#375362"
        self.window = Tk()
        self.window.title(data_dict["APP_TITLE"])
        self.window.config(padx=20, pady=20, bg=data_dict['BG_COLOR'])
        
        # TODO: create label to keep track of score
        self.score_label = Label(text=f"Score: 0", bg=data_dict['BG_COLOR'], fg=data_dict['SCORE_COLOR'], font=data_dict['SCORE_FONT'])
        self.score_label.grid(row=0, column=1)

        # TODO: create a Canvas canvas to layer image on top of window grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.quiz_question = self.canvas.create_text(150, 125, text=f"Some question text", font=data_dict["TITLE_FONT"], width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # TODO: create a button true_button on grid(row=2, column=0)
        true_button_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_button_image, highlightthickness=0, bg=data_dict['BG_COLOR'], border=5, command=self.check_answer_true)
        self.true_button.grid(row=2, column=0, padx=10, pady=10)
        
        # TODO: create a button false_button on grid(row=2, column=1)
        false_button_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_button_image, highlightthickness=0, bg=data_dict['BG_COLOR'], border=5, command=self.check_answer_false)
        self.false_button.grid(row=2, column=1, padx=10, pady=10)
        
        self.get_next_question()
        
        # TODO:window object listening for user events
        self.window.mainloop()
        
    # todo: get next question    
    def get_next_question(self):
        self.canvas.config(bg='white')
        # todo: get next question if any question left
        if self.quiz_deck.still_has_questions():
            current_question = self.quiz_deck.next_question()
            self.canvas.itemconfig(self.quiz_question, text=current_question)
        else:
            # todo: exist criteria.commented out is Angela's solution
            self.canvas.itemconfig(self.quiz_question, text='That is all for now')
            # self.true_button.config(state='disabled')
            # self.false_button.config(state='disabled')
            messagebox.showinfo(title="That's all for now", message=f"You scored:{self.quiz_deck.usr_point} Out of:{self.quiz_deck.question_number}")
            exit()
        
    # todo: check answer by passing 'True'
    def check_answer_true(self):
        self.usr_feedback(self.quiz_deck.check_answer('True'))
            
    # todo: check answer by passing 'False'
    def check_answer_false(self):
        self.usr_feedback(self.quiz_deck.check_answer('False'))
        
    # todo:change canvas background green for Correct answer,red for incorrect answer
    def usr_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.score_label.config(text=f"Score: {self.quiz_deck.usr_point}")
        self.window.after(1000, func=self.get_next_question)            
        