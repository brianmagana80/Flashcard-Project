import random
from database import get_questions

"""This file contains the code for the flashcard loop"""


def study_session(get_questions):
    random.shuffle(get_questions()) #randomizing our questions
    question_number = 0


    while question_number < len(get_questions()):                                       #if our question number is less than how many questions we have
        print(f"Question {question_number + 1}: {get_questions()[question_number][1]}") #print our questions_list using dictionary slicing
        user_answer = str(input("What's the answer to the question above? "))

        if user_answer == 'quit':
            print("Session Over")
            break
        
        elif user_answer == get_questions()[question_number][2]:                        #if user_answer is equal to the answer to it's respective question
            print("Correct!\n")
            question_number += 1                                                        #continue to the next question

        else:
            print("Incorrect. Please try again.\n")