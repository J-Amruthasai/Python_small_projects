import html
# score =0
# for i in range(len(question_bank)):
#     print(question_bank[i].question )
#     ans=input("Answer: ")
#     if(question_bank[i].answer==ans):
#         print("Correct!")
#         score +=1
#     else:
#         print("Incorrect. The correct answer is",question_bank[i].answer)
# print("The total score is ")
# print(score)


class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.scored = 0
        self.current_question = None


    def still_questions_left(self):
        if(len(self.question_list)>self.question_number):
            return True
        else:
            return False
        
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number+=1
        # html unescape entities
        question_t = html.unescape(self.current_question.question)
        return f"Q.{self.question_number}: {question_t}"
        
    def check_ans(self,user_answer):
        check_answer=self.current_question.answer
        if user_answer.lower() == check_answer.lower():
            self.scored +=1
            return True
        else:
            return False
        
    # def score(self):
    #     return f"{self.scored}/{self.question_number}"
