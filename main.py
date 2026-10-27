import mysql.connector
from datetime import datetime 
import random

"""Connecting to database"""

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="BallisLife05!",
    database="flashcards_db"
)

if mydb.is_connected():
    print("Connected!\n")
else:
    print("Connection failed")
    
    
"""Initializing cursor"""
mycursor = mydb.cursor()





"""Step 1: Create our tables"""

"""The 'questions' table consists of id, question, answer """
"""The 'history' table consists of id, attempt time, and attempt result"""
"""the 'progress' table is keeping track of how many attempts each question got, correct streak, mastery (3 correct in a row)"""
"""were going to use the random library as other answer options for the user"""

#At first I did not know what kind of database design I was going for. I knew I wanted a 'questions' table, but 
#I was confusing a progress table with a history table. At first I had a session table, but I couldn't find a reason why i would need one when i have a history table.
#I ended up fixing this problem by making the history table contain timestamps and having the progress table to see if the user is on a streak, if they mastered said question, and to see the statistics of how well a user is performing for each question.

mycursor.execute("""CREATE TABLE IF NOT EXISTS questions (
                    question_id INT PRIMARY KEY AUTO_INCREMENT,
                    question VARCHAR(128),
                    answer VARCHAR(128),
                    category VARCHAR(32)
                    )""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS history (
                    attempt_id INT PRIMARY KEY AUTO_INCREMENT, 
                    question_id INT, 
                    attempt_time TIMESTAMP NOT NULL, 
                    attempt_result VARCHAR(16), 
                    FOREIGN KEY(question_id) REFERENCES questions(question_id))""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS progress (
                    question_id INT,
                    attempts INT,
                    correct_count INT,
                    streak INT,
                    mastery bool,
                    FOREIGN KEY(question_id) REFERENCES questions(question_id))""")





"""Step 2: populate tables with values"""
#Use a list of dictionaries instead of a list of tuples since it is easier to implement new features later on
#NOTE: the tables automatically assign question ID's to each question
questions = [
    {
        "question": "What is 2 + 2?",
        "answer": "4",
        "category": "Math"
    },
    
    {
        "question": "What is 3 x 5?",
        "answer": "15",
        "category": "Math"
    },

    {
        "question": "What is 10 / 2?",
        "answer": "5",
        "category": "Math"
    },
    
    {
        "question": "What is 11 - 9?",
        "answer": "2",
        "category": "Math"
    },
    
    {
        "question": "What is 9^2?",
        "answer": "81",
        "category": "Math"
    }
        ]

# insert_questions = ("""INSERT INTO questions (question, answer, category) 
#                         VALUES (%(question)s, %(answer)s, %(category)s)""")
# mycursor.executemany(insert_questions, questions)
# mydb.commit()


"""Step 3: creating our flashcard loop"""

mycursor.execute('SELECT * FROM questions')
questions_list = mycursor.fetchall()


#the flashcard loop below works!!
random.shuffle(questions_list) #randomizing our questions
question_number = 0


while question_number < len(questions_list):                                    #if our question number is less than how many questions we have
    print(f"Question {question_number + 1}: {questions_list[question_number][1]}")  #print our questions_list using dictionary slicing
    user_answer = str(input("What's the answer to the question above? "))

    if user_answer == 'quit':
        print("Session Over")
        break
    
    elif user_answer == questions_list[question_number][2]:                       #if user_answer is equal to the answer to it's respective question
        print("Correct!")
        question_number += 1                                                    #continue to the next question

    else:
        print("Incorrect. Please try again.")