import random
from database import insert_history
from database import statistics
# from database import truncate_history
from database import get_questions 
from database import create_flashcard


"""This file contains the code for the flashcard loop"""

def menu():
    while True:
        user_option = input("""Please select an option (1-4): 
                            \n1. Study Flashcards
                            \n2. Create New Flashcard
                            \n3. View Statistics
                            \n4. Exit\n""")

        if user_option == '1':
            study_session(get_questions())
        elif user_option == '2':
            create_flashcard()
        elif user_option == '3':
            statistics()
        elif user_option == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")   
        

def study_session(questions):
    random.shuffle(questions) #randomizing our questions
    question_number = 0

    while question_number < len(questions):                                       #if our question number is less than how many questions we have
        print(f"Question {question_number + 1}: {questions[question_number][1]}") #print our questions_list using dictionary slicing
        user_answer = input("What's the answer to the question above? ")
        
        if user_answer.strip().lower() == questions[question_number][2].strip().lower():                        #if user_answer is equal to the answer to it's respective question
            print("Correct!\n")
            insert_history(questions[question_number][0], "Y")
            question_number += 1  
            
        else:
            print("Incorrect. Please try again.\n")
            insert_history(questions[question_number][0], "N")
            
            
#feature idea, have multiple answers from other questions pop up as options for the user to choose from, and if they choose the correct one, they get a point. If they choose the wrong one, they lose a point. (like kahoot)
#show statistics based on each category (the user can choose which category they want to see statistics for)