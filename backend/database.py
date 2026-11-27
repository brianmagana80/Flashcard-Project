import mysql.connector
"""This file contains the code for our database statements"""

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
    
mycursor = mydb.cursor()



"""Step 1: creating our tables"""

"""The 'questions' table consists of id, question, answer """
"""The 'history' table consists of id, attempt time, and attempt result"""

#At first I did not know what kind of database design I was going for. I knew I wanted a 'questions' table, but 
#I was confusing a progress table with a history table. At first I had a session table, but I couldn't find a reason why i would need one when i have a history table.
#I ended up fixing this problem by making the history table contain timestamps and having the progress table to see if the user is on a streak, if they mastered said question, and to see the statistics of how well a user is performing for each question.


# mycursor.execute("""CREATE TABLE IF NOT EXISTS questions (
#                     question_id INT PRIMARY KEY AUTO_INCREMENT,
#                     question VARCHAR(128),
#                     answer VARCHAR(128),
#                     category VARCHAR(32)
#                     )""")

# mycursor.execute("""CREATE TABLE IF NOT EXISTS history (
#                     attempt_id INT PRIMARY KEY AUTO_INCREMENT, 
#                     question_id INT, 
#                     attempt_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
#                     correct VARCHAR(16), 
#                     FOREIGN KEY(question_id) REFERENCES questions(question_id))""")


def get_questions(category):
    mycursor.execute(f"SELECT * FROM questions WHERE category = '{category}' ")
    return mycursor.fetchall()



def insert_history(question_id, attempt_result):
    mycursor.execute("""INSERT INTO history (question_id, correct) 
                     VALUES (%s, %s)""", (question_id, attempt_result))
    mydb.commit()
    
    
def statistics(): # number of questions, correct, incorrect, accuracy, then once session is over trunctate the table
    print("\n===== Per Question Statistics =====")
    mycursor.execute("""
                SELECT question_id, COUNT(*) AS attempts,
                SUM(correct = 'Y') AS correct_attempts
                FROM history
                GROUP BY question_id;
                                """)
    table = mycursor.fetchall()
    for row in table:
        print(f'Question_ID {row[0]}: {row[1]} attempts, {row[2]} correct attempts, {(row[2] / row[1]) * 100:.2f}% accuracy')        
    
    """Above is the statistics for each question, below is the overall statistics for the session"""

    mycursor.execute("""SELECT COUNT(attempt_id) AS attempts FROM history""")
    total_attempts = mycursor.fetchone()[0] #grab sum of rows with a value in the first column
    
    mycursor.execute("""SELECT COUNT(correct) FROM history WHERE correct = 'Y'""")
    correct = mycursor.fetchone()[0]
    incorrect = total_attempts - correct
    
    if total_attempts > 0:
        overall_accuracy = (correct / total_attempts) * 100
    else:
        overall_accuracy = 0  
          
    print("\n===== Overall Statistics =====")
    print(f'Total Attempts: {total_attempts}')
    print(f'Total Correct: {correct}')
    print(f'Total Incorrect: {incorrect}')
    print(f'Overall Accuracy: {overall_accuracy:.2f}%')
    


def truncate_history():
    mycursor.execute("""TRUNCATE TABLE history""")
    mydb.commit()
    
    
def create_flashcard():
    question = input("Enter a question: ")
    answer = input("Enter the answer: ")
    category = input("Enter the category: ")
    
    mycursor.execute("""INSERT INTO questions (question, answer, category) 
                     VALUES (%s, %s, %s)""", (question, answer, category))
    mydb.commit()
    

#select categories
def select_categories():
    mycursor.execute("SELECT DISTINCT category FROM questions")
    categories = []
    for i in mycursor.fetchall():
        categories.append(i[0])
    return categories