import html
#from config import *
class QuizBrain:
    """This class take the full list of question object and do the necessary action with still_has_action(),
     check_answer() amd next_question method"""
    def __init__(self, question_list):
        self.question_number = 0
        # todo:Bring the list of questions
        self.question_list = question_list
        self.usr_point = 0
        self.current_question = {}
        # FIXME:ValueError: string keys in translate table must be of length 1
        # self.mapping_table = str.maketrans(mapping_dict)

    def still_has_questions(self):
        """Return True if still has questions"""
        # todo:Check if any more question left,if left return True
        # print("Inside has_question")
        # print(f"self.question_number:{self.question_number}")
        # print(f"len(self.question_list):{len(self.question_list)}")
        # todo: added line for git testing
        return self.question_number < len(self.question_list)

    def check_answer(self, usr_answer: str) -> bool:
        """Take user answer as input and calculate point base on correct answer.Returns bool"""
        # todo:Check if the answer is correct/wrong
        # if self.question_list[self.question_number].q_answer.lower() == usr_answer:
        # print("Inside check_answer")
        # print(f"self.question_number:{self.question_number}")
        # print(f"self.question_list[self.question_number-1].q_answer:{self.question_list[self.question_number-1].q_text}")
        # print(f"self.question_list[self.question_number-1].q_answer:{self.question_list[self.question_number-1].q_answer}")
        if self.question_list[self.question_number-1].q_answer == usr_answer:
            # todo:Calculate point based on answer correct or wrong
            self.usr_point += 1
            print("You got it right")
            return True
        else:
            print("That's wrong")
            return False

    def next_question(self):
        """Take user answer and shows correct answer and current progress.Returns None"""
        # todo: Assign current question
        # print("Inside next_question")
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # todo:Asking usr next question after unescaping entity name and entity numbers with required display value
        # usr_answer = input(f"Q.{self.question_number}: {html.unescape(self.current_question.q_text)} (True/False): ").lower()
        # self.check_answer(usr_answer=usr_answer)
        # print(f"The correct answer was: {self.current_question.q_answer}")
        # print(f"Your current score is: {self.usr_point}/{self.question_number}\n")
        return (f"Q.{self.question_number}: {html.unescape(self.current_question.q_text)}")
