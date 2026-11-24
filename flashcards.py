import random
from database import insert_history
from database import statistics
# from database import truncate_history
from database import get_questions 
from database import create_flashcard
from database import select_categories


"""This file contains the code for the flashcard loop"""

def menu():
    while True:
        user_option = input("""Please select an option (1-4): 
                            \n1. Study Flashcards
                            \n2. Create New Flashcard
                            \n3. View Statistics
                            \n4. Exit\n""")
        print("\n")
        if user_option == '1':
            print("Select a category: \n")
            print("Available categories:")
            
            for category in select_categories():
                print(f"- {category[0]}")  # Clean up the output to show only the category name
            
            # Fetch distinct categories from the database
            
            selected_category = input()
            questions = get_questions(selected_category) #grab questions based on category
            
            if len(questions) == 0:
                print("No flashcards found for that category.")
            elif len(questions) < 4:
                print("You need at least 4 flashcards in this category. Please add more.")
            else:
                study_session(questions)
                        
            
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
        print(f"Question {question_number + 1}: {questions[question_number][1]}\n") #print our questions_list using dictionary slicing
        
        
        # correct answer
        correct_answer = questions[question_number][2]
        
        #random incorrect answer
        incorrect_answers = []
        for question in questions:
            incorrect_answers.append(question[2])
        incorrect_answers.remove(correct_answer)
        
        #shuffle 3 incorrect answers
        shuffled_incorrect_answers = random.sample(incorrect_answers, k=3)
        
        #randomize order of correct and incorrect answers
        answer_choices = [correct_answer] + shuffled_incorrect_answers
        random.shuffle(answer_choices)
        
        #display answer choices
        print(answer_choices)
        
        
        
        #Handle user input
        user_answer = input("Enter Answer: ")
        if user_answer.strip().lower() == correct_answer.strip().lower():                        #if user_answer is equal to the answer to it's respective question
            print("Correct!\n")
            insert_history(questions[question_number][0], "Y")
            question_number += 1  
            
        else:
            print("Incorrect. Please try again.\n")
            insert_history(questions[question_number][0], "N")
            
            
