from flask import Flask, render_template, request
from backend.database import get_questions, select_categories
import random

app = Flask(__name__)

# home page route
@app.route('/')
def home():
    return render_template('homepage.html')

# flashcard page route
@app.route('/study', methods=['GET', 'POST'])
def study():
    # filter through questions based on category
    questions = get_questions("Computer Science") #temporarily hard-coded
    question = questions[0][1]
    
    answer_choices = []
    correct_answer = questions[0][2]
    
    # correct or incorrect logic
    result = None
    if request.method == "POST":

        user_answer = request.form["answer"] #"answer" is the name of the button attributes in the studypage.html file. This is how we get the value of the button that was clicked.
        if user_answer == correct_answer:
            result = "Correct!"
        else:
            result = "Incorrect!"
    #random incorrect answer
    incorrect_answers = []
    for q in questions:
        incorrect_answers.append(q[2])
    incorrect_answers.remove(correct_answer)
    
    #shuffle 3 incorrect answers
    shuffled_incorrect_answers = random.sample(incorrect_answers, k=3)
    
    #randomize order of correct and incorrect answers
    answer_choices = [correct_answer] + shuffled_incorrect_answers
    random.shuffle(answer_choices)
    
    
    print(question)
    return render_template('studypage.html', question=question, answer_choices=answer_choices, result=result)


if __name__ == '__main__':
    app.run(debug=True)