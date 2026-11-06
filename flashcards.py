import random
from database import insert_history
from database import statistics
from database import truncate_history
"""This file contains the code for the flashcard loop"""


def study_session(questions):
    random.shuffle(questions) #randomizing our questions
    question_number = 0

    while question_number < len(questions):                                       #if our question number is less than how many questions we have
        print(f"Question {question_number + 1}: {questions[question_number][1]}") #print our questions_list using dictionary slicing
        user_answer = input("What's the answer to the question above? ")

        if user_answer == 'quit':
            print("Session Over")
            statistics() #call statistics function to print out the statistics of the session
            truncate_history()
            break
        
        #feature idea: if user_answer == 'reveal', print the answer, count as incorrect and move on to next question
        
        elif user_answer == questions[question_number][2]:                        #if user_answer is equal to the answer to it's respective question
            print("Correct!\n")
            
            insert_history(questions[question_number][0], "Y")
            question_number += 1  


        else:
            print("Incorrect. Please try again.\n")
            insert_history(questions[question_number][0], "N")