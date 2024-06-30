from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank =[]
for i in range(len(question_data)) :
    new_question = Question(question_data[i]["question"], question_data[i]["correct_answer"])
    question_bank.append(new_question)

# print(question_bank[0].question) # <question_model.Question object at 0x7f4fd5812af0> question model objects are created

quiz=QuizBrain(question_bank)

while quiz.still_questions_left():
    quiz.next_question()
    quiz.check_ans()
    print(f"Your current score is: {quiz.score()}")
    
print("\nYou have Completed the quiz!")
print(f"The total score is: {quiz.score()}")
quiz.score()
