import random
from database import get_questions

"""This file contains the code for the flashcard loop"""

def study_session(questions_list):
    questions = get_questions()
    random.shuffle(questions) #randomizing our questions
    question_number = 0


    while question_number < len(get_questions()):                                       #if our question number is less than how many questions we have
        print(f"Question {question_number + 1}: {questions[question_number][1]}") #print our questions_list using dictionary slicing
        user_answer = str(input("What's the answer to the question above? "))

        if user_answer == 'quit':
            print("Session Over")
            break
        
        #feature idea: if user_answer == 'reveal', print the answer
        
        elif user_answer == questions[question_number][2]:                        #if user_answer is equal to the answer to it's respective question
            print("Correct!\n")
            question_number += 1                                                        #continue to the next question

        else:
            print("Incorrect. Please try again.\n")