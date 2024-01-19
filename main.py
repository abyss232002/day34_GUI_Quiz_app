
# Powered by https://opentdb.com/api.php
from question_model import Question
from data import Data
from quiz_brain import QuizBrain
from ui import QuizInterface

new_q_list = []

# todo:create data object to get question_data from opentdb,defualt number of question 10,default type boolean(True/False)
data = Data(amount=10,category=27,difficulty='easy')
#print(data.question_data)
for i in range(len(data.question_data)):
    new_q = Question(q_text=data.question_data[i]['question'], q_answer=data.question_data[i]['correct_answer'])
    new_q_list.append(new_q)

quiz_deck = QuizBrain(question_list=new_q_list)
# todo:create UI for the quiz app
quiz_ui = QuizInterface(quiz_deck)
# while quiz_deck.still_has_questions():
#     quiz_deck.next_question()
# print("You've completed the quiz")
# print(f"Your final score was: {quiz_deck.usr_point}/{quiz_deck.question_number}")