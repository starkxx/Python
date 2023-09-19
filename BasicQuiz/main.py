from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# Creating an empty list and Looping through questions from question_data
# Assigning text for every text part and answer for answer part
# Create a new object calle new_question=Question(...,...)
# Append these questions to the question_bank

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was :{quiz.score} /{quiz.question_number}")