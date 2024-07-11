# the importing of ui.py file does all the work

from question_model import Question
from data import questions
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = [Question(question["question"], question["correct_answer"]) for question in questions]

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
